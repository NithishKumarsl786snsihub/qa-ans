"use client";

import { useState } from "react";
import { Check, Copy, ChevronDown, ChevronUp, FileCode, Layers, Sparkles } from "lucide-react";

interface FormattedPromptProps {
  prompt: string;
  keywords?: string[];
  studyMode?: boolean;
  isSingleChoiceYesNo?: boolean;
}

function CodeBlock({ code, language = "code" }: { code: string; language?: string }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  // Simple syntax highlighter for common keywords
  const formatSyntax = (raw: string) => {
    const lines = raw.split("\n");
    return lines.map((line, lineIdx) => {
      // Highlight comments
      if (line.trim().startsWith("#") || line.trim().startsWith("//")) {
        return (
          <div key={lineIdx} className="code-line comment">
            {line}
          </div>
        );
      }

      // Highlight python/bicep/json keywords
      const tokens = line.split(/(\s+|[(),={}:"'])/);
      return (
        <div key={lineIdx} className="code-line">
          {tokens.map((token, tokIdx) => {
            const isKeyword = [
              "import", "from", "def", "class", "return", "if", "else", "elif",
              "while", "for", "in", "not", "and", "or", "try", "except", "resource",
              "properties", "existing", "scope", "target", "authType", "metadata",
              "az", "create", "set", "enable", "True", "False", "None", "as"
            ].includes(token);

            const isString = /^["'].*["']$/.test(token);
            const isFn = /^[a-zA-Z_]\w*(?=\()/.test(token);

            if (isKeyword) {
              return <span key={tokIdx} className="kw-keyword">{token}</span>;
            }
            if (isString) {
              return <span key={tokIdx} className="kw-string">{token}</span>;
            }
            if (isFn) {
              return <span key={tokIdx} className="kw-fn">{token}</span>;
            }
            return token;
          })}
        </div>
      );
    });
  };

  return (
    <div className="code-window">
      <div className="code-window-header">
        <span className="code-lang-badge">
          <FileCode size={13} style={{ marginRight: 6 }} />
          {language.toUpperCase()}
        </span>
        <button type="button" className="copy-code-btn" onClick={handleCopy} title="Copy code">
          {copied ? (
            <>
              <Check size={13} style={{ marginRight: 4 }} />
              Copied!
            </>
          ) : (
            <>
              <Copy size={13} style={{ marginRight: 4 }} />
              Copy
            </>
          )}
        </button>
      </div>
      <pre className="code-window-body">
        <code>{formatSyntax(code)}</code>
      </pre>
    </div>
  );
}

function highlightTextKeywords(text: string, keywords: string[] = []) {
  if (!keywords.length) return text;
  const escaped = keywords
    .filter(Boolean)
    .sort((a, b) => b.length - a.length)
    .map((word) => word.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));

  if (!escaped.length) return text;

  const pattern = new RegExp(`(${escaped.join("|")})`, "gi");
  const parts = text.split(pattern);

  return parts.map((part, index) => {
    const matched = keywords.some((word) => word.toLowerCase() === part.toLowerCase());
    return matched ? (
      <mark className="keyword" key={`${part}-${index}`}>
        {part}
      </mark>
    ) : (
      part
    );
  });
}

export function FormattedPrompt({
  prompt,
  keywords = [],
  studyMode = false,
  isSingleChoiceYesNo = false
}: FormattedPromptProps) {
  const [caseStudyExpanded, setCaseStudyExpanded] = useState(false);

  if (!prompt) return null;

  // Check if prompt has a Case Study block
  const caseStudyMatch = prompt.match(/(?:HOTSPOT\s*\n*)?(?:DRAG DROP\s*\n*)?Case Study[\s\S]*?(?=Technical Requirements|Business Requirements|Security and Compliance Requirements|You need to|How should you|Which|What should you|Note:|$)/i);

  let caseStudyText = "";
  let mainPromptText = prompt;

  if (caseStudyMatch && prompt.includes("Contoso")) {
    caseStudyText = caseStudyMatch[0].trim();
    mainPromptText = prompt.replace(caseStudyText, "").trim();
  }

  // Detect code blocks or syntax snippets in mainPromptText
  const codeBlocks: { text: string; language: string }[] = [];
  let extractedMainText = mainPromptText;

  // Extract explicit ```code``` blocks if present
  if (mainPromptText.includes("```")) {
    extractedMainText = mainPromptText.replace(/```(\w+)?\n([\s\S]*?)```/g, (_, lang, code) => {
      codeBlocks.push({ text: code.trim(), language: lang || "code" });
      return "[[CODE_BLOCK]]";
    });
  } else {
    // Detect raw inline code snippets like python/bicep scripts
    const rawCodePattern = /(?:import time[\s\S]*?print \(video\.status\)|from azure\.identity[\s\S]*?print \(f "Retrieved agent: \{agent\.name\}"\)|az cognitiveservices account create[\s\S]*?\}\},|def get_self_harm_severity[\s\S]*?return result\.severity|for brand in image_analysis\.brands:[\s\S]*?brand\.rectangle\.h"\)|resource existingKeyVault[\s\S]*?ResourceId: existingKeyVault\.id)/g;
    
    extractedMainText = mainPromptText.replace(rawCodePattern, (match) => {
      let lang = "python";
      if (match.includes("az cognitiveservices")) lang = "bash";
      if (match.includes("resource existingKeyVault")) lang = "bicep";
      codeBlocks.push({ text: match.trim(), language: lang });
      return "[[CODE_BLOCK]]";
    });
  }

  const textSegments = extractedMainText.split("[[CODE_BLOCK]]");

  return (
    <div className="formatted-prompt-container">
      {/* Case Study Collapsible Card */}
      {caseStudyText ? (
        <div className="case-study-card">
          <button
            type="button"
            className="case-study-header"
            onClick={() => setCaseStudyExpanded(!caseStudyExpanded)}
          >
            <div className="case-study-title">
              <Layers size={16} className="case-study-icon" />
              <span>Case Study Scenario & Background (Contoso, Ltd)</span>
            </div>
            <div className="case-study-toggle">
              <span className="case-study-badge">
                {caseStudyExpanded ? "Hide Details" : "Show Details"}
              </span>
              {caseStudyExpanded ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
            </div>
          </button>

          {caseStudyExpanded && (
            <div className="case-study-body">
              <pre className="case-study-text">{caseStudyText}</pre>
            </div>
          )}
        </div>
      ) : null}

      {/* Main Prompt Text and Code Blocks */}
      <div className="prompt-body-content">
        {textSegments.map((segment, idx) => {
          const cleanSeg = segment.trim();
          return (
            <div key={idx} className="prompt-segment">
              {cleanSeg && (
                <div className="prompt-text-paragraph">
                  {cleanSeg.split("\n\n").map((para: string, pIdx: number) => {
                    // Check for Solution: [...] in Single-Choice Yes/No questions during Study Mode
                    const solutionMatch = para.match(/^Solution:\s*(.*)/i);
                    const isSolutionPara = solutionMatch || para.startsWith("Solution:");

                    if (studyMode && isSingleChoiceYesNo && isSolutionPara) {
                      const solText = solutionMatch ? solutionMatch[1] : para.replace(/^Solution:\s*/i, "");
                      return (
                        <div key={pIdx} className="proposed-solution-highlight-card">
                          <div className="solution-card-header">
                            <Sparkles size={16} className="solution-sparkle-icon" />
                            <span>Proposed Solution Under Evaluation</span>
                            <span className="study-badge">Study Mode Highlight</span>
                          </div>
                          <div className="solution-card-body">
                            <strong className="solution-prefix">Solution:</strong>{" "}
                            <span className="solution-text">
                              {highlightTextKeywords(solText, keywords)}
                            </span>
                          </div>
                        </div>
                      );
                    }

                    return (
                      <p key={pIdx} className="prompt-p">
                        {highlightTextKeywords(para, keywords)}
                      </p>
                    );
                  })}
                </div>
              )}

              {codeBlocks[idx] && (
                <CodeBlock
                  code={codeBlocks[idx].text}
                  language={codeBlocks[idx].language}
                />
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
