"use client";

import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  CheckCircle2,
  ClipboardList,
  RotateCcw,
  Settings,
  X
} from "lucide-react";
import { useMemo, useState } from "react";
import { ConfirmModal, type ConfirmModalProps } from "./ConfirmModal";
import { Option, Question, questions } from "../lib/questions";
import { FormattedPrompt } from "./FormattedPrompt";

type AppTab = "study" | "test";
type TestMode = "same-same" | "random-same" | "random-random";
type AnswerDisplay = "immediate" | "end";
type TestQuestion = Question & { options: Option[] };
type TestState = {
  mode: TestMode;
  answerDisplay: AnswerDisplay;
  questions: TestQuestion[];
  answers: Record<string, string[]>;
  submitted: Record<string, boolean>;
  currentIndex: number;
  startedAt: number;
  completedAt?: number;
};

type ConfirmRequest = Pick<
  ConfirmModalProps,
  "title" | "message" | "confirmLabel" | "cancelLabel" | "tone"
> & {
  onConfirm: () => void;
};

const selfCorrect = "__SELF_CORRECT";
const selfIncorrect = "__SELF_INCORRECT";

function shuffle<T>(items: T[]) {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function highlightKeywords(text: string, keywords: string[]) {
  const escaped = keywords
    .filter(Boolean)
    .sort((a, b) => b.length - a.length)
    .map((word) => word.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));

  if (!escaped.length) return text;

  const pattern = new RegExp(`(${escaped.join("|")})`, "gi");
  return text.split(pattern).map((part, index) => {
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

function sameSet(a: string[] = [], b: string[] = []) {
  return a.length === b.length && a.every((item) => b.includes(item));
}

function correctAnswerText(question: Question) {
  if (question.answerItems?.length) {
    return question.answerItems.map((item) => `${item.label}: ${item.value}`).join("; ");
  }
  if (question.correctOptionIds.length && question.options.length) {
    return question.correctOptionIds
      .map((id) => {
        const option = question.options.find((item) => item.id === id);
        return option ? `${id}. ${option.text}` : id;
      })
      .join(", ");
  }
  return question.answer || "No answer text was extractable from the PDF.";
}

function isQuestionCorrect(question: Question, selectedIds: string[] = []) {
  if (question.answerItems?.some((item) => item.options?.length)) {
    return question.answerItems.every((item, index) => selectedIds[index] === item.value);
  }
  if (!question.options.length) return selectedIds.includes(selfCorrect);
  return sameSet(selectedIds, question.correctOptionIds);
}

function isQuestionUnanswered(question: Question, selectedIds: string[] = []) {
  return !selectedIds.length;
}

function formatDuration(ms: number) {
  const seconds = Math.max(0, Math.floor(ms / 1000));
  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  return `${mins}m ${secs.toString().padStart(2, "0")}s`;
}

function buildTestQuestions(mode: TestMode): TestQuestion[] {
  const base = mode === "same-same" ? [...questions] : shuffle(questions);
  return base.map((question) => ({
    ...question,
    options: mode === "random-random" ? shuffle(question.options) : [...question.options]
  }));
}

export function QuestionApp() {
  const [activeTab, setActiveTab] = useState<AppTab>("study");
  const [studyIndex, setStudyIndex] = useState(0);
  const [reviewed, setReviewed] = useState<Record<string, boolean>>({});
  const [configOpen, setConfigOpen] = useState(false);
  const [testMode, setTestMode] = useState<TestMode>("same-same");
  const [answerDisplay, setAnswerDisplay] = useState<AnswerDisplay>("immediate");
  const [testState, setTestState] = useState<TestState | null>(null);
  const [confirmRequest, setConfirmRequest] = useState<ConfirmRequest | null>(null);

  const studyQuestion = questions[studyIndex];

  const startTest = () => {
    setTestState({
      mode: testMode,
      answerDisplay,
      questions: buildTestQuestions(testMode),
      answers: {},
      submitted: {},
      currentIndex: 0,
      startedAt: Date.now()
    });
    setConfigOpen(false);
    setActiveTab("test");
  };

  const guardedTabChange = (tab: AppTab) => {
    if (testState && !testState.completedAt && tab !== "test") {
      setConfirmRequest({
        title: "Leave Test Mode?",
        message: "A test is in progress. You can leave this view and keep the test progress in the background.",
        confirmLabel: "Leave",
        cancelLabel: "Stay",
        onConfirm: () => setActiveTab(tab)
      });
      return;
    }
    setActiveTab(tab);
  };

  return (
    <main className="app-shell">
      <header className="topbar">
        <div className="topbar-inner">
          <div className="brand-block">
            <h1>Question Revision & Assessment</h1>
            <p>Internal study flow with answer reasoning and controlled test randomization.</p>
          </div>
          <nav className="tabs" aria-label="Primary">
            <button
              className={`tab-button ${activeTab === "study" ? "active" : ""}`}
              onClick={() => guardedTabChange("study")}
            >
              <BookOpen size={18} /> Study Mode
            </button>
            <button
              className={`tab-button ${activeTab === "test" ? "active" : ""}`}
              onClick={() => guardedTabChange("test")}
            >
              <ClipboardList size={18} /> Test Mode
            </button>
          </nav>
        </div>
      </header>

      <div className="page">
        {activeTab === "study" ? (
          <StudyMode
            question={studyQuestion}
            currentIndex={studyIndex}
            reviewed={Boolean(reviewed[studyQuestion.id])}
            onToggleReviewed={() =>
              setReviewed((current) => ({
                ...current,
                [studyQuestion.id]: !current[studyQuestion.id]
              }))
            }
            onMove={(next) => setStudyIndex(Math.min(Math.max(next, 0), questions.length - 1))}
            reviewedCount={Object.values(reviewed).filter(Boolean).length}
            reviewedMap={reviewed}
          />
        ) : (
          <TestModeView
            testState={testState}
            onOpenConfig={() => setConfigOpen(true)}
            onUpdate={setTestState}
            onRequestConfirm={setConfirmRequest}
          />
        )}
      </div>

      {configOpen && (
        <ConfigModal
          testMode={testMode}
          answerDisplay={answerDisplay}
          onModeChange={setTestMode}
          onDisplayChange={setAnswerDisplay}
          onClose={() => setConfigOpen(false)}
          onStart={startTest}
        />
      )}
      <ConfirmModal
        open={Boolean(confirmRequest)}
        title={confirmRequest?.title || ""}
        message={confirmRequest?.message || ""}
        confirmLabel={confirmRequest?.confirmLabel}
        cancelLabel={confirmRequest?.cancelLabel}
        tone={confirmRequest?.tone}
        onConfirm={() => {
          const action = confirmRequest?.onConfirm;
          setConfirmRequest(null);
          action?.();
        }}
        onCancel={() => setConfirmRequest(null)}
      />
    </main>
  );
}

function StudyMode({
  question,
  currentIndex,
  reviewed,
  reviewedCount,
  reviewedMap,
  onToggleReviewed,
  onMove
}: {
  question: Question;
  currentIndex: number;
  reviewed: boolean;
  reviewedCount: number;
  reviewedMap: Record<string, boolean>;
  onToggleReviewed: () => void;
  onMove: (index: number) => void;
}) {
  return (
    <>
      <ProgressHeader
        label={`Question ${currentIndex + 1} of ${questions.length}`}
        progress={(currentIndex + 1) / questions.length}
        right={`${reviewedCount} reviewed`}
      />
      <div className="question-layout">
        <QuestionPanel
          question={question}
          selectedIds={
            question.answerItems?.some((item) => item.options?.length)
              ? question.answerItems.map((item) => item.value)
              : question.correctOptionIds
          }
          submitted
          showCorrect
          studyMode
        />
        <aside className="side-panel">
          <h2 className="section-title">Revision State</h2>
          <p>{reviewed ? "This question is marked reviewed." : "This question still needs review."}</p>
          <div className="button-row">
            <button className={reviewed ? "danger-button" : "primary-button"} onClick={onToggleReviewed}>
              {reviewed ? <X size={17} /> : <CheckCircle2 size={17} />}
              {reviewed ? "Mark Not Reviewed" : "Mark Reviewed"}
            </button>
          </div>
          <div className="button-row">
            <button className="secondary-button" onClick={() => onMove(currentIndex - 1)} disabled={currentIndex === 0}>
              <ArrowLeft size={17} /> Previous
            </button>
            <button
              className="primary-button"
              onClick={() => onMove(currentIndex + 1)}
              disabled={currentIndex === questions.length - 1}
            >
              Next <ArrowRight size={17} />
            </button>
          </div>
          <div className="question-map">
            {questions.map((item, index) => (
              <button
                key={item.id}
                className={`map-button ${index === currentIndex ? "active" : ""} ${
                  reviewedMap[item.id] ? "done" : ""
                }`}
                onClick={() => onMove(index)}
                aria-label={`Go to question ${index + 1}`}
              >
                {index + 1}
              </button>
            ))}
          </div>
        </aside>
      </div>
    </>
  );
}

function TestModeView({
  testState,
  onOpenConfig,
  onUpdate,
  onRequestConfirm
}: {
  testState: TestState | null;
  onOpenConfig: () => void;
  onUpdate: (state: TestState | null) => void;
  onRequestConfirm: (request: ConfirmRequest) => void;
}) {
  if (!testState) {
    return (
      <section className="panel empty-state">
        <h2>Start a Controlled Test</h2>
        <p>
          Choose original or randomized question order, keep or shuffle answer options, and decide when answer
          feedback should appear.
        </p>
        <button className="primary-button" onClick={onOpenConfig}>
          <Settings size={18} /> Start Test
        </button>
      </section>
    );
  }

  if (testState.completedAt) {
    return <Results state={testState} onRestart={onOpenConfig} onReset={() => onUpdate(null)} />;
  }

  const question = testState.questions[testState.currentIndex];
  const selectedIds = testState.answers[question.id] || [];
  const submitted = Boolean(testState.submitted[question.id]);
  const immediate = testState.answerDisplay === "immediate";
  const answeredCount = Object.keys(testState.answers).filter((id) => testState.answers[id]?.length).length;

  const selectOption = (optionId: string) => {
    if (submitted && immediate) return;
    const nextSelected =
      question.correctOptionIds.length > 1
        ? selectedIds.includes(optionId)
          ? selectedIds.filter((id) => id !== optionId)
          : [...selectedIds, optionId]
        : [optionId];

    onUpdate({
      ...testState,
      answers: { ...testState.answers, [question.id]: nextSelected }
    });
  };

  const selectScenarioOption = (val: string, itemIndex: number) => {
    if (submitted && immediate) return;
    const current = [...(testState.answers[question.id] || [])];
    current[itemIndex] = val;
    onUpdate({
      ...testState,
      answers: { ...testState.answers, [question.id]: current }
    });
  };

  const submitCurrent = () => {
    onUpdate({
      ...testState,
      submitted: { ...testState.submitted, [question.id]: true }
    });
  };

  const selfAssessCurrent = (correct: boolean) => {
    onUpdate({
      ...testState,
      answers: { ...testState.answers, [question.id]: [correct ? selfCorrect : selfIncorrect] },
      submitted: { ...testState.submitted, [question.id]: true }
    });
  };

  const finishTest = () => {
    onRequestConfirm({
      title: "Submit Test?",
      message: "Unanswered questions will be counted in the result. You can review question numbers before submitting.",
      confirmLabel: "Submit Test",
      cancelLabel: "Keep Working",
      tone: "danger",
      onConfirm: () => onUpdate({ ...testState, completedAt: Date.now() })
    });
  };

  const hasInteractiveOptions = Boolean(
    question.options.length || question.answerItems?.some((item) => item.options?.length)
  );

  return (
    <>
      <ProgressHeader
        label={`Question ${testState.currentIndex + 1} of ${testState.questions.length}`}
        progress={(testState.currentIndex + 1) / testState.questions.length}
        right={`${answeredCount} answered`}
      />
      <div className="question-layout">
        <QuestionPanel
          question={question}
          selectedIds={selectedIds}
          submitted={submitted}
          showCorrect={immediate && submitted}
          onSelect={selectOption}
          onSelectScenario={selectScenarioOption}
        />
        <aside className="side-panel">
          <h2 className="section-title">Test Progress</h2>
          <p>
            Mode: {modeLabel(testState.mode)}
            <br />
            Answers: {testState.answerDisplay === "immediate" ? "Immediate feedback" : "Final review only"}
          </p>
          <div className="button-row">
            <button
              className="secondary-button"
              onClick={() => onUpdate({ ...testState, currentIndex: testState.currentIndex - 1 })}
              disabled={testState.currentIndex === 0}
            >
              <ArrowLeft size={17} /> Previous
            </button>
            <button
              className="secondary-button"
              onClick={() => onUpdate({ ...testState, currentIndex: testState.currentIndex + 1 })}
              disabled={testState.currentIndex === testState.questions.length - 1}
            >
              Next <ArrowRight size={17} />
            </button>
            {(!submitted || testState.answerDisplay === "end") && (
              hasInteractiveOptions ? (
                <button className="primary-button" onClick={submitCurrent} disabled={!selectedIds.length}>
                  Submit Answer
                </button>
              ) : (
                <>
                  <button className="primary-button" onClick={() => selfAssessCurrent(true)}>
                    Mark Correct
                  </button>
                  <button className="secondary-button" onClick={() => selfAssessCurrent(false)}>
                    Mark Incorrect
                  </button>
                </>
              )
            )}
            <button className="danger-button" onClick={finishTest}>
              Finish Test
            </button>
          </div>
          <div className="question-map">
            {testState.questions.map((item, index) => (
              <button
                key={item.id}
                className={`map-button ${index === testState.currentIndex ? "active" : ""} ${
                  testState.answers[item.id]?.length ? "done" : ""
                }`}
                onClick={() => onUpdate({ ...testState, currentIndex: index })}
              >
                {index + 1}
              </button>
            ))}
          </div>
        </aside>
      </div>
    </>
  );
}

function QuestionPanel({
  question,
  selectedIds,
  submitted,
  showCorrect,
  studyMode = false,
  onSelect,
  onSelectScenario
}: {
  question: TestQuestion;
  selectedIds: string[];
  submitted: boolean;
  showCorrect: boolean;
  studyMode?: boolean;
  onSelect?: (optionId: string) => void;
  onSelectScenario?: (value: string, index: number) => void;
}) {
  const isCorrect = submitted && isQuestionCorrect(question, selectedIds);
  const hasScenarioOptions = Boolean(question.answerItems?.some((item) => item.options?.length));

  const isSingleChoiceYesNo =
    question.type === "Single Choice" &&
    (question.prompt.includes("Does this meet the goal?") ||
      (question.options.length === 2 &&
        question.options.some((o) => o.text === "Yes") &&
        question.options.some((o) => o.text === "No")));

  return (
    <section className="panel">
      <div className="question-kicker">
        <span className="pill">Question {question.number}</span>
        <span className="pill">{question.type}</span>
        {question.sourcePages?.length ? <span className="pill">Pages {question.sourcePages.join(", ")}</span> : null}
        {studyMode && <span className="pill success">Correct answer visible</span>}
        {!studyMode && submitted && (
          <span className={`pill ${isCorrect ? "success" : "warning"}`}>
            {isCorrect ? "Correct" : "Needs review"}
          </span>
        )}
      </div>
      <FormattedPrompt
        prompt={question.prompt}
        keywords={question.keywords}
        studyMode={studyMode}
        isSingleChoiceYesNo={isSingleChoiceYesNo}
      />
      {question.warnings?.length ? (
        <div className="reason-box" style={{ marginTop: 14 }}>
          <h3 className="section-title">Extraction Notes</h3>
          <ul className="reason-list">
            {question.warnings.map((warning) => (
              <li key={warning}>{warning}</li>
            ))}
          </ul>
        </div>
      ) : null}
      {question.uiFormat === "yes-no-matrix" && question.answerItems?.length ? (
        <div className="matrix-container">
          <table className="matrix-table">
            <thead>
              <tr>
                <th>Statements</th>
                <th className="center">Yes</th>
                <th className="center">No</th>
              </tr>
            </thead>
            <tbody>
              {question.answerItems.map((item, index) => {
                const selectedVal = selectedIds[index] || "";
                const isYesCorrect = showCorrect && item.value.toLowerCase() === "yes";
                const isNoCorrect = showCorrect && item.value.toLowerCase() === "no";

                return (
                  <tr key={item.label}>
                    <td>{item.label}</td>
                    <td className="center">
                      <button
                        type="button"
                        className={`matrix-radio-btn ${selectedVal === "Yes" ? "selected" : ""} ${
                          isYesCorrect ? "correct-target" : ""
                        }`}
                        onClick={() => onSelectScenario?.("Yes", index)}
                        disabled={submitted && showCorrect && !studyMode}
                      />
                    </td>
                    <td className="center">
                      <button
                        type="button"
                        className={`matrix-radio-btn ${selectedVal === "No" ? "selected" : ""} ${
                          isNoCorrect ? "correct-target" : ""
                        }`}
                        onClick={() => onSelectScenario?.("No", index)}
                        disabled={submitted && showCorrect && !studyMode}
                      />
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      ) : question.uiFormat === "drag-drop" && question.answerItems?.length ? (
        <DragDropQuestionView
          question={question}
          selectedIds={selectedIds}
          submitted={submitted}
          showCorrect={showCorrect}
          studyMode={studyMode}
          onSelectScenario={onSelectScenario}
        />
      ) : hasScenarioOptions ? (
        <div className="scenario-grid">
          <h3 className="section-title" style={{ gridColumn: "1 / -1", margin: "10px 0 0" }}>
            Answer Area (Select Dropdown Options)
          </h3>
          {question.answerItems?.map((item, index) => {
            const selectedValue = selectedIds[index] || "";
            const isItemCorrect = (submitted || studyMode) && selectedValue === item.value;

            return (
              <div
                key={item.label}
                className={`choice-card ${showCorrect && isItemCorrect ? "correct" : ""}`}
              >
                <label style={{ display: "block", width: "100%" }}>
                  <strong>{item.label}:</strong>
                  <select
                    className="scenario-select"
                    value={selectedValue}
                    onChange={(e) => onSelectScenario?.(e.target.value, index)}
                    disabled={submitted && showCorrect && !studyMode}
                  >
                    <option value="">-- Select Choice --</option>
                    {item.options?.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                </label>
                {showCorrect && (
                  <p className="correct-value-note">
                    Correct: <strong>{item.value}</strong>
                  </p>
                )}
              </div>
            );
          })}
        </div>
      ) : question.options.length ? (
        <div className="options">
          {question.options.map((option) => {
            if (!option.id) {
              throw new Error(`Question ${question.id} contains an option without a valid option.id.`);
            }
            const correct = question.correctOptionIds.includes(option.id);
            const selected = selectedIds.includes(option.id);
            const incorrectSelection = submitted && selected && !correct;
            return (
              <button
                className={`option-row ${selected ? "selected" : ""} ${
                  showCorrect && correct ? "correct" : ""
                } ${showCorrect && incorrectSelection ? "incorrect" : ""}`}
                key={option.id}
                onClick={() => onSelect?.(option.id)}
                disabled={!onSelect}
              >
                <span className="option-key">{option.id}</span>
                <span>{highlightKeywords(option.text, question.keywords)}</span>
              </button>
            );
          })}
        </div>
      ) : (
        <div className="reason-box" style={{ marginTop: 18 }}>
          <h3 className="section-title">Answer Area</h3>
          <p>
            This question uses a visual answer area, drag-drop mapping, Yes/No matrix, or dropdown-style answer.
            Use the structured answer below for revision and self-check testing.
          </p>
        </div>
      )}
      {showCorrect && (
        <div className="explanation-grid">
          <div className="reason-box">
            <h3 className="section-title">Correct Answer</h3>
            {question.answerItems?.length ? (
              <ul className="reason-list">
                {question.answerItems.map((item) => (
                  <li key={`${item.label}-${item.value}`}>
                    <strong>{item.label}:</strong> {item.value}
                  </li>
                ))}
              </ul>
            ) : (
              <p>{correctAnswerText(question)}</p>
            )}
          </div>
          <div className="reason-box">
            <h3 className="section-title">Explanation</h3>
            <p>{question.explanation || "No separate explanation text was extractable from the PDF."}</p>
          </div>
        </div>
      )}
      {showCorrect && question.reasoning.length > 0 && (
        <div className="reason-box" style={{ marginTop: 14 }}>
          <h3 className="section-title">Reasoning Points</h3>
          <ul className="reason-list">
            {question.reasoning.map((point) => (
              <li key={point}>{point}</li>
            ))}
          </ul>
        </div>
      )}
      {showCorrect && question.options.length > question.correctOptionIds.length && (
        <div className="reason-box" style={{ marginTop: 14 }}>
          <h3 className="section-title">Why Other Options Are Incorrect</h3>
          <ul className="reason-list">
            {question.options
              .filter((option) => !question.correctOptionIds.includes(option.id))
              .map((option) => (
                <li key={option.id}>
                  <strong>{option.id}:</strong> {option.whyIncorrect || "No option-specific explanation was extractable."}
                </li>
              ))}
          </ul>
        </div>
      )}
    </section>
  );
}

function DragDropQuestionView({
  question,
  selectedIds,
  submitted,
  showCorrect,
  studyMode,
  onSelectScenario
}: {
  question: TestQuestion;
  selectedIds: string[];
  submitted: boolean;
  showCorrect: boolean;
  studyMode?: boolean;
  onSelectScenario?: (value: string, index: number) => void;
}) {
  const [activeChip, setActiveChip] = useState<string | null>(null);
  const [draggedOverIndex, setDraggedOverIndex] = useState<number | null>(null);

  const availableOptions = Array.from(
    new Set(question.answerItems?.flatMap((item) => item.options || [item.value]) || [])
  );

  const handleDragStart = (e: React.DragEvent, opt: string) => {
    e.dataTransfer.setData("text/plain", opt);
    e.dataTransfer.effectAllowed = "copy";
  };

  const handleDrop = (e: React.DragEvent, slotIndex: number) => {
    e.preventDefault();
    setDraggedOverIndex(null);
    const val = e.dataTransfer.getData("text/plain") || activeChip;
    if (val) {
      onSelectScenario?.(val, slotIndex);
      setActiveChip(null);
    }
  };

  const handleChipClick = (opt: string) => {
    if (submitted && showCorrect && !studyMode) return;
    if (activeChip === opt) {
      setActiveChip(null);
    } else {
      setActiveChip(opt);
      const emptyIndex = question.answerItems?.findIndex((_, idx) => !selectedIds[idx]);
      if (emptyIndex !== undefined && emptyIndex !== -1) {
        onSelectScenario?.(opt, emptyIndex);
        setActiveChip(null);
      }
    }
  };

  return (
    <div className="drag-split-container">
      <div className="drag-pool-panel">
        <div className="drag-panel-title">Configurations (Available Options)</div>
        <p className="drag-instruction">Drag an option card or click to select & place into target slot.</p>
        {availableOptions.map((opt) => (
          <div
            key={opt}
            className={`drag-chip ${activeChip === opt ? "selected" : ""}`}
            draggable={!submitted || studyMode}
            onDragStart={(e) => handleDragStart(e, opt)}
            onClick={() => handleChipClick(opt)}
          >
            <span className="drag-chip-handle">::</span>
            <span>{opt}</span>
          </div>
        ))}
      </div>
      <div className="drag-target-panel">
        <div className="drag-panel-title">Answer Area</div>
        {question.answerItems?.map((item, index) => {
          const selectedVal = selectedIds[index] || "";
          const isCorrectTarget = showCorrect && selectedVal === item.value;
          const isDragOver = draggedOverIndex === index;

          return (
            <div key={item.label} className="drop-slot-row">
              <span className="drop-slot-label">{item.label}:</span>
              <div
                className={`drop-slot-box ${selectedVal ? "filled" : ""} ${
                  isDragOver ? "drag-over" : ""
                } ${isCorrectTarget ? "correct-target" : ""}`}
                onDragOver={(e) => {
                  e.preventDefault();
                  e.dataTransfer.dropEffect = "copy";
                  setDraggedOverIndex(index);
                }}
                onDragLeave={() => setDraggedOverIndex(null)}
                onDrop={(e) => handleDrop(e, index)}
                onClick={() => {
                  if (activeChip) {
                    onSelectScenario?.(activeChip, index);
                    setActiveChip(null);
                  }
                }}
              >
                {selectedVal ? (
                  <div className="placed-chip">
                    <span className="drag-chip-handle">::</span>
                    <span>{selectedVal}</span>
                    {(!submitted || studyMode) && (
                      <button
                        type="button"
                        className="clear-chip-btn"
                        onClick={(e) => {
                          e.stopPropagation();
                          onSelectScenario?.("", index);
                        }}
                      >
                        <X size={14} />
                      </button>
                    )}
                  </div>
                ) : (
                  <select
                    className="scenario-select"
                    style={{ margin: 0 }}
                    value={selectedVal}
                    onChange={(e) => onSelectScenario?.(e.target.value, index)}
                    disabled={submitted && showCorrect && !studyMode}
                  >
                    <option value="">-- Drag option here or Select --</option>
                    {item.options?.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                )}
              </div>
              {showCorrect && (
                <p className="correct-value-note">
                  Correct Answer: <strong>{item.value}</strong>
                </p>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

function ConfigModal({
  testMode,
  answerDisplay,
  onModeChange,
  onDisplayChange,
  onClose,
  onStart
}: {
  testMode: TestMode;
  answerDisplay: AnswerDisplay;
  onModeChange: (mode: TestMode) => void;
  onDisplayChange: (display: AnswerDisplay) => void;
  onClose: () => void;
  onStart: () => void;
}) {
  const modes: Array<{ value: TestMode; title: string; text: string }> = [
    {
      value: "same-same",
      title: "Same Questions + Same Answer Order",
      text: "Questions remain in the original order and options remain unchanged."
    },
    {
      value: "random-same",
      title: "Random Questions + Same Answer Order",
      text: "Questions are shuffled while answer options keep their original order."
    },
    {
      value: "random-random",
      title: "Random Questions + Random Answer Order",
      text: "Questions and options are shuffled while answer mapping stays tied to option ids."
    }
  ];

  return (
    <div className="modal-backdrop" role="dialog" aria-modal="true">
      <section className="modal-panel">
        <div className="modal-header">
          <div>
            <h2>Test Configuration</h2>
            <p className="brand-block" style={{ margin: "6px 0 0", color: "var(--muted)" }}>
              Select question order, option order, and answer reveal behavior.
            </p>
          </div>
          <button className="icon-button" onClick={onClose} aria-label="Close configuration">
            <X size={18} />
          </button>
        </div>
        <h3 className="section-title">Question Mode</h3>
        <div className="config-grid">
          {modes.map((mode) => (
            <div className={`choice-card ${testMode === mode.value ? "active" : ""}`} key={mode.value}>
              <label>
                <input
                  type="radio"
                  checked={testMode === mode.value}
                  onChange={() => onModeChange(mode.value)}
                />
                <span>
                  <strong>{mode.title}</strong>
                  {mode.text}
                </span>
              </label>
            </div>
          ))}
        </div>
        <h3 className="section-title" style={{ marginTop: 18 }}>
          Answer Display
        </h3>
        <div className="config-grid">
          {[
            ["immediate", "Show answer immediately after each question"],
            ["end", "Show results only after completing the test"]
          ].map(([value, label]) => (
            <div className={`choice-card ${answerDisplay === value ? "active" : ""}`} key={value}>
              <label>
                <input
                  type="radio"
                  checked={answerDisplay === value}
                  onChange={() => onDisplayChange(value as AnswerDisplay)}
                />
                <span>{label}</span>
              </label>
            </div>
          ))}
        </div>
        <div className="button-row">
          <button className="primary-button" onClick={onStart}>
            Start Test
          </button>
          <button className="secondary-button" onClick={onClose}>
            Cancel
          </button>
        </div>
      </section>
    </div>
  );
}

function Results({
  state,
  onRestart,
  onReset
}: {
  state: TestState;
  onRestart: () => void;
  onReset: () => void;
}) {
  const stats = useMemo(() => {
    const total = state.questions.length;
    const correct = state.questions.filter((question) => isQuestionCorrect(question, state.answers[question.id] || [])).length;
    const unanswered = state.questions.filter((question) =>
      isQuestionUnanswered(question, state.answers[question.id] || [])
    ).length;
    const incorrect = total - correct - unanswered;
    const percent = Math.round((correct / total) * 100);
    return { total, correct, incorrect, unanswered, percent };
  }, [state]);

  return (
    <>
      <div className="toolbar">
        <div>
          <h2 style={{ margin: 0 }}>Final Result</h2>
          <p style={{ margin: "6px 0 0", color: "var(--muted)" }}>
            Completed in {formatDuration((state.completedAt || Date.now()) - state.startedAt)}
          </p>
        </div>
        <div className="button-row" style={{ margin: 0 }}>
          <button className="primary-button" onClick={onRestart}>
            <RotateCcw size={17} /> New Test
          </button>
          <button className="secondary-button" onClick={onReset}>
            Clear Result
          </button>
        </div>
      </div>
      <div className="stats-grid">
        <Stat label="Total" value={stats.total} />
        <Stat label="Correct" value={stats.correct} />
        <Stat label="Incorrect" value={stats.incorrect} />
        <Stat label="Unanswered" value={stats.unanswered} />
        <Stat label="Percentage" value={`${stats.percent}%`} />
      </div>
      <div className="review-list">
        {state.questions.map((question, index) => {
          const selected = state.answers[question.id] || [];
          const correct = isQuestionCorrect(question, selected);
          const selectedText =
            selected.includes(selfCorrect)
              ? "Self-marked correct"
              : selected.includes(selfIncorrect)
                ? "Self-marked incorrect"
                : selected.map((id) => question.options.find((option) => option.id === id)?.text || id).join(", ") ||
                  "Unanswered";
          const correctText = correctAnswerText(question);
          return (
            <section className="panel" key={question.id}>
              <div className="question-kicker">
                <span className="pill">Review {index + 1}</span>
                <span className={`pill ${correct ? "success" : "warning"}`}>
                  {correct ? "Correct" : selected.length ? "Incorrect" : "Unanswered"}
                </span>
              </div>
              <h3 className="question-title" style={{ fontSize: 19 }}>
                {question.prompt}
              </h3>
              <div className="explanation-grid" style={{ marginTop: 14 }}>
                <div className="reason-box">
                  <h4 className="section-title">Selected Answer</h4>
                  <p>{selectedText}</p>
                </div>
                <div className="reason-box">
                  <h4 className="section-title">Correct Answer</h4>
                  <p>{correctText}</p>
                </div>
              </div>
              {!correct && (
                <div className="reason-box" style={{ marginTop: 14 }}>
                  <h4 className="section-title">Explanation</h4>
                  <p>{question.explanation}</p>
                </div>
              )}
            </section>
          );
        })}
      </div>
    </>
  );
}

function ProgressHeader({ label, progress, right }: { label: string; progress: number; right: string }) {
  return (
    <div className="toolbar">
      <div className="progress-wrap">
        <div className="progress-meta">
          <span>{label}</span>
          <span>{right}</span>
        </div>
        <div className="progress-track">
          <div className="progress-fill" style={{ width: `${Math.round(progress * 100)}%` }} />
        </div>
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string | number }) {
  return (
    <div className="stat">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function modeLabel(mode: TestMode) {
  if (mode === "same-same") return "Same questions, same options";
  if (mode === "random-same") return "Random questions, same options";
  return "Random questions, random options";
}
