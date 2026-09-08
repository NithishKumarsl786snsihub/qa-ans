const fs = require("fs");

const path = "lib/questions.ts";
let src = fs.readFileSync(path, "utf8");
const header = src.match(/^[\s\S]*?export const questions: Question\[] = /)?.[0];
if (!header) throw new Error("Could not find questions export");
const body = src.slice(header.length).replace(/;\s*$/, "");
const questions = eval(body);

const phraseBank = [
  "Azure AI Search",
  "Azure OpenAI",
  "Microsoft Foundry",
  "Foundry Agent Service",
  "Application Insights",
  "OpenTelemetry",
  "OTEL_SERVICE_NAME",
  "DefaultAzureCredential",
  "managed identity",
  "system-assigned managed identity",
  "user-assigned managed identity",
  "Cognitive Services OpenAI User",
  "Storage Blob Data Reader",
  "Key Vault Secrets User",
  "Prompt Shields",
  "image moderation",
  "protected material",
  "PII",
  "self-harm",
  "violence",
  "groundedness",
  "Groundedness and Relevance",
  "RAG evaluator",
  "Retrieval Augmented Generation",
  "model cascade",
  "token usage",
  "tracing",
  "RequestResponse",
  "Model Availability Rate",
  "Provisioned Utilization",
  "tool_choice",
  "OpenAPI",
  "API key security scheme",
  "Connection1",
  "workflow",
  "ask_question",
  "human approval",
  "Content Understanding",
  "Document Intelligence",
  "Document Layout",
  "Document Extraction",
  "semantic search",
  "vector search",
  "Azure OpenAI Embedding",
  "Text Split",
  "ContentFormat.MARKDOWN",
  "Custom Vision",
  "Speech",
  "custom speech project ID",
  "base model",
  "SSML",
  "phonemes",
  "Translator",
  "Immersive Reader",
  "DALL-E",
  "serverless API",
  "video generation",
  "OpenAI",
  "CognitiveServices",
  "AzureKeyVault",
  "AccountManagedIdentity",
  "AIServices",
  "--encryption",
  "AnalyzeTextOptions",
  "analyze_text",
  "Object projection",
  "Table projection",
  "agent memory",
  "persistent storage",
  "File search",
  "Code interpreter",
  "Grounding with Bing Search",
  "sequential template",
  "Ask a question node",
  "Spotlighting",
  "Azure Login action",
  "OpenID Connect",
  "customer-managed key",
  "read-only access",
  "query key",
  "delete compromised key",
  "model deployment",
  "deployment type",
  "version update policy",
  "Standard",
  "Global Standard",
  "Global Provisioned"
];

const stopValues = new Set([
  "",
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "yes",
  "no",
  "answer",
  "correct option",
  "correct options",
  "true",
  "false",
  "step 1",
  "step 2",
  "step 3"
]);

function cleanText(value) {
  return String(value || "")
    .replace(/[`*#]/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\.$/, "");
}

function addKeyword(list, seen, value) {
  const cleaned = cleanText(value);
  const key = cleaned.toLowerCase();
  if (!cleaned || stopValues.has(key) || seen.has(key)) return;
  if (cleaned.length < 3 || cleaned.length > 72) return;
  seen.add(key);
  list.push(cleaned);
}

function shortAnswerCue(text) {
  const cleaned = cleanText(text)
    .replace(/^the\s+/i, "")
    .replace(/^a\s+/i, "")
    .replace(/^an\s+/i, "");
  if (cleaned.length <= 58) return cleaned;
  const beforePunctuation = cleaned.split(/[.;:]/)[0].trim();
  if (beforePunctuation && beforePunctuation.length <= 58) return beforePunctuation;
  return cleaned.split(/\s+/).slice(0, 7).join(" ");
}

function extractNeedCue(prompt) {
  const match = prompt.match(/You need to\s+([^.\n]+)/i);
  return match ? shortAnswerCue(match[1]) : "";
}

for (const question of questions) {
  const keywords = [];
  const seen = new Set();
  const prompt = question.prompt || "";
  const answerText = [
    question.answer,
    ...(question.answerItems || []).flatMap((item) => [item.label, item.value]),
    ...(question.correctOptionIds || []).map((id) => question.options?.find((option) => option.id === id)?.text || "")
  ].join(" ");
  const searchable = `${prompt} ${answerText}`.toLowerCase();

  for (const item of question.answerItems || []) {
    addKeyword(keywords, seen, shortAnswerCue(item.value));
    addKeyword(keywords, seen, shortAnswerCue(item.label));
  }

  for (const id of question.correctOptionIds || []) {
    const option = question.options?.find((item) => item.id === id);
    if (option) addKeyword(keywords, seen, shortAnswerCue(option.text));
  }

  for (const phrase of phraseBank) {
    if (searchable.includes(phrase.toLowerCase())) addKeyword(keywords, seen, phrase);
  }

  addKeyword(keywords, seen, extractNeedCue(prompt));

  if (!keywords.length && question.answer) addKeyword(keywords, seen, shortAnswerCue(question.answer));
  if (!keywords.length) addKeyword(keywords, seen, question.type);

  question.keywords = keywords.slice(0, 8);
}

fs.writeFileSync(path, `${header}${JSON.stringify(questions, null, 2)};\n`);
