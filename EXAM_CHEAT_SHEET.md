# 🔥 AI Apps & Agents on Azure — Master Pattern-Recognition Cheat Sheet

> **Exam Strategy**: Don't read whole paragraphs. Scan for **Primary Triggers** $\rightarrow$ **Mark Answer in 5 Seconds**.

---

### 📌 Question 1 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Deployment type**: `Standard`, **Version update policy**: `Once the current version expires` |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Deployment type**: `Standard`, **Version update policy**: `Once the current version expires` |
| **"without requiring reserved throughput"** | $\rightarrow$ **Deployment type**: `Standard`, **Version update policy**: `Once the current version expires` |
| **"variable customer support traffic"** | $\rightarrow$ **Deployment type**: `Standard`, **Version update policy**: `Once the current version expires` |

> 🧠 **Memory Anchor**: *Deployment Type: Selected as Standard because the workload requires dynamic scaling for variable traffic without reserved throughput capacity (eliminating Provi...*


---

### 📌 Question 2 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Option B** (prompt shields) |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Option B** (prompt shields) |
| **"without requiring reserved throughput"** | $\rightarrow$ **Option B** (prompt shields) |
| **"variable customer support traffic"** | $\rightarrow$ **Option B** (prompt shields) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B*


---

### 📌 Question 3 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Add a connection to the Azure AI Search resource."** | $\rightarrow$ **Option C** (Add a connection to the Azure AI Search resource.) |
| **"centrally manage the Azure AI Search credentials"** | $\rightarrow$ **Option C** (Add a connection to the Azure AI Search resource.) |
| **"connection to the Azure AI Search resource"** | $\rightarrow$ **Option C** (Add a connection to the Azure AI Search resource.) |

> 🧠 **Memory Anchor**: *Technical Justification for Recommending Option C For centrally managing Azure AI Search credentials across multiple agents in Project1, Option C: Add a  connec...*


---

### 📌 Question 4 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"enable_content_recording=False"** | $\rightarrow$ **The LangChain service will appear in Traces without configuring a tracer.**: `No`, **Setting different OTEL_SERVICE_NAME values separates the services in Application Insights.**: `Yes`, **When using enable_content_recording=False, prompts and tool data will be captured in the telemetry.**: `No` |
| **"OTEL_SERVICE_NAME"** | $\rightarrow$ **The LangChain service will appear in Traces without configuring a tracer.**: `No`, **Setting different OTEL_SERVICE_NAME values separates the services in Application Insights.**: `Yes`, **When using enable_content_recording=False, prompts and tool data will be captured in the telemetry.**: `No` |

> 🧠 **Memory Anchor**: *Statement 1: No OpenTelemetry tracing requires explicit configuration to start capturing data*


---

### 📌 Question 5 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Pro mode's core advantage is cross-file reasoning"** | $\rightarrow$ **Pipeline1**: `Single-file task in standard mode`, **Pipeline2**: `Multi-file task in pro mode` |
| **"Single-file task in standard mode"** | $\rightarrow$ **Pipeline1**: `Single-file task in standard mode`, **Pipeline2**: `Multi-file task in pro mode` |
| **"Multi-file task in pro mode"** | $\rightarrow$ **Pipeline1**: `Single-file task in standard mode`, **Pipeline2**: `Multi-file task in pro mode` |
| **"Pipeline1"** | $\rightarrow$ **Pipeline1**: `Single-file task in standard mode`, **Pipeline2**: `Multi-file task in pro mode` |

> 🧠 **Memory Anchor**: *Pipeline1 (Single-file task in standard mode): This is correct for workflows processing independent, standalone documents one by one*


---

### 📌 Question 6 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"DefaultAzureCredential"** | $\rightarrow$ **First Dropdown (credential =)**: `DefaultAzureCredential`, **Second Dropdown (response = openai_client.responses.)**: `create` |
| **"managed identity"** | $\rightarrow$ **First Dropdown (credential =)**: `DefaultAzureCredential`, **Second Dropdown (response = openai_client.responses.)**: `create` |
| **"Azure OpenAI"** | $\rightarrow$ **First Dropdown (credential =)**: `DefaultAzureCredential`, **Second Dropdown (response = openai_client.responses.)**: `create` |
| **"standard"** | $\rightarrow$ **First Dropdown (credential =)**: `DefaultAzureCredential`, **Second Dropdown (response = openai_client.responses.)**: `create` |

> 🧠 **Memory Anchor**: *First Dropdown: DefaultAzureCredential Second Dropdown: create Credential Initialization: The scenario specifies authentication using a Microsoft Entra managed ...*


---

### 📌 Question 7 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"If/else condition expression"** | $\rightarrow$ **If/else condition expression**: `Not(IsBlank(Local.Var01))`, **Send message expression**: `Upper(Local.Var01)` |
| **"Not(IsBlank(Local.Var01"** | $\rightarrow$ **If/else condition expression**: `Not(IsBlank(Local.Var01))`, **Send message expression**: `Upper(Local.Var01)` |
| **"Send message expression"** | $\rightarrow$ **If/else condition expression**: `Not(IsBlank(Local.Var01))`, **Send message expression**: `Upper(Local.Var01)` |
| **"Upper(Local.Var01"** | $\rightarrow$ **If/else condition expression**: `Not(IsBlank(Local.Var01))`, **Send message expression**: `Upper(Local.Var01)` |

> 🧠 **Memory Anchor**: *If/else condition expression: Not(IsBlank(Local.Var01)) Send message expression: Upper(Local.Var01) If/else condition expression: The requirement is to ensure t...*


---

### 📌 Question 8 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Select User input, Output, Tool response, and Tool call; set Action to Block"** | $\rightarrow$ **Guardrails configuration**: `Select User input, Output, Tool response, and Tool call; set Action to Block`, **Storage access configuration**: `System-assigned managed identity assigned Storage Blob Data Reader` |
| **"System-assigned managed identity assigned Storage Blob Data Reader"** | $\rightarrow$ **Guardrails configuration**: `Select User input, Output, Tool response, and Tool call; set Action to Block`, **Storage access configuration**: `System-assigned managed identity assigned Storage Blob Data Reader` |
| **"System-assigned managed identity"** | $\rightarrow$ **Guardrails configuration**: `Select User input, Output, Tool response, and Tool call; set Action to Block`, **Storage access configuration**: `System-assigned managed identity assigned Storage Blob Data Reader` |
| **"principle of least privilege"** | $\rightarrow$ **Guardrails configuration**: `Select User input, Output, Tool response, and Tool call; set Action to Block`, **Storage access configuration**: `System-assigned managed identity assigned Storage Blob Data Reader` |

> 🧠 **Memory Anchor**: *Guardrails Select User input, Output, Tool response, and Tool call and set Action to Block*


---

### 📌 Question 9 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"a workflow"** | $\rightarrow$ **Option A** (a workflow) |

> 🧠 **Memory Anchor**: *A*


---

### 📌 Question 10 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"the custom speech project ID"** | $\rightarrow$ **Option B** (the custom speech project ID) |
| **"fine-tuning"** | $\rightarrow$ **Option B** (the custom speech project ID) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B The correct option to set the project property to resolve the invalid project ID error when using Azure Speech  in...*


---

### 📌 Question 11 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"approval == "approved"** | $\rightarrow$ **Approval step type**: `ask_question`, **Refund condition**: `approval == "approved"` |
| **"ask_question"** | $\rightarrow$ **Approval step type**: `ask_question`, **Refund condition**: `approval == "approved"` |

> 🧠 **Memory Anchor**: *ask_question: In declarative agent workflows, ask_question is used to explicitly pause execution and collect external feedback or manual intervention (such as h...*


---

### 📌 Question 12 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Speech recognition requests will fall back to the most recent base model for the"** | $\rightarrow$ **Option C** (Speech recognition requests will fall back to the most recent base model for the) |
| **"less suitable: B"** | $\rightarrow$ **Option C** (Speech recognition requests will fall back to the most recent base model for the) |
| **"less suitable: D"** | $\rightarrow$ **Option C** (Speech recognition requests will fall back to the most recent base model for the) |
| **"less suitable: A"** | $\rightarrow$ **Option C** (Speech recognition requests will fall back to the most recent base model for the) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: C The correct answer is C*


---

### 📌 Question 13 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Cognitive Services OpenAI User"** | $\rightarrow$ **Option B** (Cognitive Services OpenAI User) |
| **"Principle of Least Privilege"** | $\rightarrow$ **Option B** (Cognitive Services OpenAI User) |
| **"DefaultAzureCredential"** | $\rightarrow$ **Option B** (Cognitive Services OpenAI User) |
| **"Azure OpenAI"** | $\rightarrow$ **Option B** (Cognitive Services OpenAI User) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B (Cognitive Services OpenAI User) The correct role-based access control (RBAC) role to assign to the developers for...*


---

### 📌 Question 14 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"tool_choice= “required”"** | $\rightarrow$ **Option A** (tool_choice= “required”) |
| **"standard"** | $\rightarrow$ **Option A** (tool_choice= “required”) |

> 🧠 **Memory Anchor**: *A*


---

### 📌 Question 15 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Groundedness evaluation metrics"** | $\rightarrow$ **Unsupported responses**: `Groundedness evaluation metrics`, **Policy violations**: `Risk and safety metrics` |
| **"Risk and safety metrics"** | $\rightarrow$ **Unsupported responses**: `Groundedness evaluation metrics`, **Policy violations**: `Risk and safety metrics` |
| **"Unsupported responses"** | $\rightarrow$ **Unsupported responses**: `Groundedness evaluation metrics`, **Policy violations**: `Risk and safety metrics` |
| **"evaluation metrics"** | $\rightarrow$ **Unsupported responses**: `Groundedness evaluation metrics`, **Policy violations**: `Risk and safety metrics` |

> 🧠 **Memory Anchor**: *Unsupported responses Groundedness evaluation metrics Policy violations: Risk and safety metrics Unsupported responses: When an AI model generates responses con...*


---

### 📌 Question 16 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option C (Visual Block"** | $\rightarrow$ **Option C** (Option C (Visual Block)) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: C To ensure the key value from the connection is included automatically whenever the OpenAPI tool is invoked for the...*


---

### 📌 Question 17 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Use a model cascade that routes the requests to different models."** | $\rightarrow$ **Option B** (Use a model cascade that routes the requests to different models.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B Why B is the Best Option:Using a model cascade that routes requests to different models is the optimal  approach f...*


---

### 📌 Question 18 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Model Availability Rate and Provisioned Utilization"** | $\rightarrow$ **Metrics to enable**: `Model Availability Rate and Provisioned Utilization`, **Diagnostic log to collect**: `Request Response` |
| **"Diagnostic log to collect"** | $\rightarrow$ **Metrics to enable**: `Model Availability Rate and Provisioned Utilization`, **Diagnostic log to collect**: `Request Response` |
| **"Metrics to enable"** | $\rightarrow$ **Metrics to enable**: `Model Availability Rate and Provisioned Utilization`, **Diagnostic log to collect**: `Request Response` |
| **"Request Response"** | $\rightarrow$ **Metrics to enable**: `Model Availability Rate and Provisioned Utilization`, **Diagnostic log to collect**: `Request Response` |

> 🧠 **Memory Anchor**: *Metrics to enable : Model Availability Rate and Provisioned Utilization Model Availability Rate isolates whether service errors or operation drop-offs are cause...*


---

### 📌 Question 19 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Evaluation metrics"** | $\rightarrow$ **Option D** (token usage) |
| **"token usage"** | $\rightarrow$ **Option D** (token usage) |

> 🧠 **Memory Anchor**: *Technical Justification for Choosing D*


---

### 📌 Question 20 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"tool_choice"** | $\rightarrow$ **Parameter**: `tool_choice`, **Value**: `required` |
| **"standard"** | $\rightarrow$ **Parameter**: `tool_choice`, **Value**: `required` |
| **"required"** | $\rightarrow$ **Parameter**: `tool_choice`, **Value**: `required` |

> 🧠 **Memory Anchor**: *Set tool_choice to required Configure the tool to authenticate by: Using a distinct agent identity bound to the client application Set tool_choice to (required)...*


---

### 📌 Question 21 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"it directly addresses the issue by"** | $\rightarrow$ **Option D** (Connect the tool to Connection1.) |
| **"Connect the tool to Connection1."** | $\rightarrow$ **Option D** (Connect the tool to Connection1.) |
| **"tool invocation"** | $\rightarrow$ **Option D** (Connect the tool to Connection1.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer D Correct Answer: D*


---

### 📌 Question 22 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Tracing To address the reported issues with the Microsoft Foundry project's customer support agent"** | $\rightarrow$ **Option D** (Tracing To address the reported issues with the Microsoft Foundry project's customer support agent, the chosen) |
| **"tool invocation"** | $\rightarrow$ **Option D** (Tracing To address the reported issues with the Microsoft Foundry project's customer support agent, the chosen) |

> 🧠 **Memory Anchor**: *Technical Justification for Choosing D*


---

### 📌 Question 23 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Prompt Shield"** | $\rightarrow$ **Option B** (No) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B*


---

### 📌 Question 24 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"standard"** | $\rightarrow$ **Option B** (No) |

> 🧠 **Memory Anchor**: *Technical Justification for Solution Evaluation Scenario Recap: Mitigate risks in a multimodal AI generative model by preventing unsafe image uploads that  embe...*


---

### 📌 Question 25 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Prompt shields"** | $\rightarrow$ **Option B** (No) |
| **"Prompt Shield"** | $\rightarrow$ **Option B** (No) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B*


---

### 📌 Question 26 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"B"** | $\rightarrow$ **Option B** (No) |

> 🧠 **Memory Anchor**: *Technical Justification for Solution Evaluation Scenario Recap: Mitigate risks associated with unsafe image uploads and hidden instructions in a multimodal  AI ...*


---

### 📌 Question 27 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Option D** (a groundedness evaluator) |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Option D** (a groundedness evaluator) |
| **"without requiring reserved throughput"** | $\rightarrow$ **Option D** (a groundedness evaluator) |
| **"variable customer support traffic"** | $\rightarrow$ **Option D** (a groundedness evaluator) |

> 🧠 **Memory Anchor**: *D*


---

### 📌 Question 28 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Option A** (Modify the system message instructions.) |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Option A** (Modify the system message instructions.) |
| **"Modify the system message instructions."** | $\rightarrow$ **Option A** (Modify the system message instructions.) |
| **"without requiring reserved throughput"** | $\rightarrow$ **Option A** (Modify the system message instructions.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: A*


---

### 📌 Question 29 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"a large language model (LLM"** | $\rightarrow$ **Option D** (a large language model (LLM)) |

> 🧠 **Memory Anchor**: *Technical Justification for Choosing D: a Large Language Model (LLM) Requirements Analysis and Model Selection The customer support solution requires a model th...*


---

### 📌 Question 30 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"tool_choice"** | $\rightarrow$ **Parameter**: `tool_choice`, **Value**: `required` |
| **"Parameter"** | $\rightarrow$ **Parameter**: `tool_choice`, **Value**: `required` |
| **"required"** | $\rightarrow$ **Parameter**: `tool_choice`, **Value**: `required` |
| **"Value"** | $\rightarrow$ **Parameter**: `tool_choice`, **Value**: `required` |

> 🧠 **Memory Anchor**: *"tool_choice": This parameter key overrides the default tool execution behavior for a specific thread run*


---

### 📌 Question 31 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Configure an Azure AI Search connection in Project1 and reference the connection in each application"** | $\rightarrow$ **Option B** (Configure an Azure AI Search connection in Project1 and reference the connection in each application) |
| **"Managed Identity"** | $\rightarrow$ **Option B** (Configure an Azure AI Search connection in Project1 and reference the connection in each application) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B Why B is the Best Option: Meets Requirement 1: Multiple Client Applications - Configuring an Azure AI Search conne...*


---

### 📌 Question 32 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Grounding with Bing Search"** | $\rightarrow$ **Access up-to-date public information**: `Grounding with Bing Search`, **Perform calculations**: `Code interpreter`, **Retrieve uploaded documents**: `File search` |
| **"Perform calculations"** | $\rightarrow$ **Access up-to-date public information**: `Grounding with Bing Search`, **Perform calculations**: `Code interpreter`, **Retrieve uploaded documents**: `File search` |
| **"Code interpreter"** | $\rightarrow$ **Access up-to-date public information**: `Grounding with Bing Search`, **Perform calculations**: `Code interpreter`, **Retrieve uploaded documents**: `File search` |
| **"File search"** | $\rightarrow$ **Access up-to-date public information**: `Grounding with Bing Search`, **Perform calculations**: `Code interpreter`, **Retrieve uploaded documents**: `File search` |

> 🧠 **Memory Anchor**: *Access up-to-date information (Grounding with Bing Search): This native tool allows the agent to execute real-time web queries to retrieve current information a...*


---

### 📌 Question 33 — Multiple Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option B (Visual Block"** | $\rightarrow$ **Correct options**: `B, C` |
| **"Option C (Visual Block"** | $\rightarrow$ **Correct options**: `B, C` |
| **"Standard"** | $\rightarrow$ **Correct options**: `B, C` |
| **"B, C"** | $\rightarrow$ **Correct options**: `B, C` |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: BC To implement end-to-end tracing for capturing latency breakdowns and exceptions across agent runs in a Microsoft ...*


---

### 📌 Question 34 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Create and reuse a conversation by storing the conversation’s ID and supplying the ID on subsequent"** | $\rightarrow$ **Option A** (Create and reuse a conversation by storing the conversation’s ID and supplying the ID on subsequent) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Option (A) To ensure the Microsoft Foundry Agent Service automatically reloads the complete history on each new turn  for re...*


---

### 📌 Question 35 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"temperature"** | $\rightarrow$ **temperature**: `1`, **output_config effort**: `low` |
| **"standard"** | $\rightarrow$ **temperature**: `1`, **output_config effort**: `low` |
| **"low"** | $\rightarrow$ **temperature**: `1`, **output_config effort**: `low` |

> 🧠 **Memory Anchor**: *temperature :1 When enabling extended or adaptive reasoning via the thinking parameter ( "type": "enabled" ), API rules mandate that the temperature must be set...*


---

### 📌 Question 36 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"agentic Retrieval Augmented Generation (RAG"** | $\rightarrow$ **Option B** (agentic Retrieval Augmented Generation (RAG)) |
| **"Retrieval Augmented Generation"** | $\rightarrow$ **Option B** (agentic Retrieval Augmented Generation (RAG)) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B - Agentic Retrieval Augmented Generation (RAG) Why B (Agentic Retrieval Augmented Generation) is the Best Choice: ...*


---

### 📌 Question 37 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Agent memory that uses persistent storage"** | $\rightarrow$ **Retain user preferences across chat sessions**: `Agent memory that uses persistent storage`, **Contextual grounding during chats**: `File search tool` |
| **"Contextual grounding during chats"** | $\rightarrow$ **Retain user preferences across chat sessions**: `Agent memory that uses persistent storage`, **Contextual grounding during chats**: `File search tool` |
| **"File search tool"** | $\rightarrow$ **Retain user preferences across chat sessions**: `Agent memory that uses persistent storage`, **Contextual grounding during chats**: `File search tool` |

> 🧠 **Memory Anchor**: *To retain user preferences across conversations, use: Agent memory that uses persistent storage*


---

### 📌 Question 38 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Add a retry evaluation before the responses are returned."** | $\rightarrow$ **Option A** (Add a retry evaluation before the responses are returned.) |
| **"Retrieval Augmented Generation"** | $\rightarrow$ **Option A** (Add a retry evaluation before the responses are returned.) |
| **"relevance"** | $\rightarrow$ **Option A** (Add a retry evaluation before the responses are returned.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: A Why A is the best option:To improve response completeness in the context of an agent generating summaries from ret...*


---

### 📌 Question 39 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Implement a retry policy that uses exponential backoff and jitter."** | $\rightarrow$ **Option C** (Implement a retry policy that uses exponential backoff and jitter.) |
| **"Azure OpenAI"** | $\rightarrow$ **Option C** (Implement a retry policy that uses exponential backoff and jitter.) |
| **"rate limit"** | $\rightarrow$ **Option C** (Implement a retry policy that uses exponential backoff and jitter.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer (C) Why C is the Best Option:Implementing a retry policy with exponential backoff and jitter (Option C) is the  most ...*


---

### 📌 Question 40 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Azure Login action that uses OpenID Connect (OIDC"** | $\rightarrow$ **Authentication method**: `Azure Login action that uses OpenID Connect (OIDC)`, **Workflow action on failure**: `Fail` |
| **"Workflow action on failure"** | $\rightarrow$ **Authentication method**: `Azure Login action that uses OpenID Connect (OIDC)`, **Workflow action on failure**: `Fail` |
| **"Authentication method"** | $\rightarrow$ **Authentication method**: `Azure Login action that uses OpenID Connect (OIDC)`, **Workflow action on failure**: `Fail` |
| **"content safety"** | $\rightarrow$ **Authentication method**: `Azure Login action that uses OpenID Connect (OIDC)`, **Workflow action on failure**: `Fail` |

> 🧠 **Memory Anchor**: *Authentication method An Azure Login action that uses OpenID Connect (OIDC)) When connecting an automated external runner or automation pipeline to Azure resour...*


---

### 📌 Question 41 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Yes"** | $\rightarrow$ **Option A** (Yes) |

> 🧠 **Memory Anchor**: *Technical Justification for Solution Review Scenario Recap: Enhance response completeness for a Microsoft Foundry agent generating summaries from policy documen...*


---

### 📌 Question 42 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Yes"** | $\rightarrow$ **Option A** (Yes) |

> 🧠 **Memory Anchor**: *Technical Justification for Solution Evaluation Scenario Recap: Enhance response completeness in a Microsoft Foundry agent that generates summaries from policy ...*


---

### 📌 Question 43 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Fine-Tuning"** | $\rightarrow$ **Option B** (No) |
| **"relevance"** | $\rightarrow$ **Option B** (No) |

> 🧠 **Memory Anchor**: *Technical Justification for Solution Evaluation Scenario Recap: Enhancing response completeness for a Microsoft Foundry agent that generates summaries from poli...*


---

### 📌 Question 44 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"B"** | $\rightarrow$ **Option B** (No) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B*


---

### 📌 Question 45 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Enable mask_inpainting and supply both the input image and a mask indicating which part of the image to"** | $\rightarrow$ **Option D** (Enable mask_inpainting and supply both the input image and a mask indicating which part of the image to) |

> 🧠 **Memory Anchor**: *Technical Justification for Configuring the Image-Editing Workflow Correct Answer: D*


---

### 📌 Question 46 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Apply a mask-based inpainting edit to the part of the image that contains the logo"** | $\rightarrow$ **Option A** (Apply a mask-based inpainting edit to the part of the image that contains the logo.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: A Why A is the best option:Applying a mask-based inpainting edit to the part of the image that contains the  logo (O...*


---

### 📌 Question 47 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"prebuilt-layout The correct option for the given requirement is D"** | $\rightarrow$ **Option D** (prebuilt-layout The correct option for the given requirement is D) |

> 🧠 **Memory Anchor**: *Justification for Choosing Option D: prebuilt-layout The correct option for the given requirement is D: prebuilt-layout*


---

### 📌 Question 48 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Set the input_fidelity parameter to high."** | $\rightarrow$ **Option A** (Set the input_fidelity parameter to high.) |
| **"groundedness"** | $\rightarrow$ **Option A** (Set the input_fidelity parameter to high.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: A Why A is the Best Choice:Setting the input_fidelity parameter to high is the most appropriate action to ensure gen...*


---

### 📌 Question 49 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Additional mitigation"** | $\rightarrow$ **Prompt Shields action**: `Set action to block`, **Additional mitigation**: `Enable Spotlighting` |
| **"Prompt Shields action"** | $\rightarrow$ **Prompt Shields action**: `Set action to block`, **Additional mitigation**: `Enable Spotlighting` |
| **"Set action to block"** | $\rightarrow$ **Prompt Shields action**: `Set action to block`, **Additional mitigation**: `Enable Spotlighting` |
| **"Enable Spotlighting"** | $\rightarrow$ **Prompt Shields action**: `Set action to block`, **Additional mitigation**: `Enable Spotlighting` |

> 🧠 **Memory Anchor**: *Prompt shields action: Set action to block*


---

### 📌 Question 50 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Implement image moderation."** | $\rightarrow$ **Option D** (Implement image moderation.) |
| **"prompt shields"** | $\rightarrow$ **Option D** (Implement image moderation.) |
| **"relevance"** | $\rightarrow$ **Option D** (Implement image moderation.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: D Why D (Implement image moderation) is the best option:Implementing image moderation is the most suitable  choice f...*


---

### 📌 Question 51 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"prompt shields for documents"** | $\rightarrow$ **Option B** (prompt shields for documents) |
| **"malicious instructions"** | $\rightarrow$ **Option B** (prompt shields for documents) |
| **"Prompt Shields"** | $\rightarrow$ **Option B** (prompt shields for documents) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B - Prompt Shields for Documents Why B is the best option:Prompt Shields for Documents is specifically designed to s...*


---

### 📌 Question 52 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"an Azure Content Understanding in Foundry Tools analyzer"** | $\rightarrow$ **Option D** (an Azure Content Understanding in Foundry Tools analyzer) |
| **"Azure OpenAI"** | $\rightarrow$ **Option D** (an Azure Content Understanding in Foundry Tools analyzer) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: D To address the requirement of processing mixed-format documents (containing scanned text, tables, and  multicolumn...*


---

### 📌 Question 53 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Azure Content Understanding in Foundry Tools"** | $\rightarrow$ **Option B** (Azure Content Understanding in Foundry Tools) |

> 🧠 **Memory Anchor**: *Justification for Correct Answer: B - Azure Content Understanding in Foundry Tools The correct solution for the given scenario is B*


---

### 📌 Question 54 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Use advanced data parsing to reingest the documents."** | $\rightarrow$ **Option A** (Use advanced data parsing to reingest the documents.) |
| **"Retrieval Augmented Generation"** | $\rightarrow$ **Option A** (Use advanced data parsing to reingest the documents.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Option (A) The correct configuration for the ingestion job, given the requirements, is A*


---

### 📌 Question 55 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"an indexer to extract image data into a normalized_images collection"** | $\rightarrow$ **Option A** (an indexer to extract image data into a normalized_images collection) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: A The correct indexing approach to ensure images are extracted into a structure suitable for the built-in Optical Ch...*


---

### 📌 Question 56 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Option C** (Azure Content Understanding in Foundry Tools) |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Option C** (Azure Content Understanding in Foundry Tools) |
| **"Azure Content Understanding in Foundry Tools"** | $\rightarrow$ **Option C** (Azure Content Understanding in Foundry Tools) |
| **"without requiring reserved throughput"** | $\rightarrow$ **Option C** (Azure Content Understanding in Foundry Tools) |

> 🧠 **Memory Anchor**: *Technical Justification for Invoice Review Solution Recommendation Correct Option: C*


---

### 📌 Question 57 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Enable estimateFieldSourceAndConfidence."** | $\rightarrow$ **Option C** (Enable estimateFieldSourceAndConfidence.) |
| **"Retrieval Augmented Generation"** | $\rightarrow$ **Option C** (Enable estimateFieldSourceAndConfidence.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: C To address the requirements of including per-field confidence scores and source grounding to locations  within the...*


---

### 📌 Question 58 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Use real-time speech to text to process streaming audio input."** | $\rightarrow$ **Option D** (Use real-time speech to text to process streaming audio input.) |
| **"best choice and why the others are less"** | $\rightarrow$ **Option D** (Use real-time speech to text to process streaming audio input.) |

> 🧠 **Memory Anchor**: *Technical Justification for the Correct Option (D) To meet the requirement of transcribing live phone calls with near-real-time transcription (within a few seco...*


---

### 📌 Question 59 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Use real-time speech to text for incoming audio and text to speech for agent responses"** | $\rightarrow$ **Option B** (Use real-time speech to text for incoming audio and text to speech for agent responses.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B Why B is the Best Option: Real-time Processing: Option B utilizes real-time speech to text, which is essential for...*


---

### 📌 Question 60 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Split the mixed-language segments into single-language segments and translate each segment separately"** | $\rightarrow$ **Option B** (Split the mixed-language segments into single-language segments and translate each segment separately.) |
| **"best and why other options are less"** | $\rightarrow$ **Option B** (Split the mixed-language segments into single-language segments and translate each segment separately.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: B To address the issue of incomplete or incorrect translations for mixed-language segments in App1, the most  effect...*


---

### 📌 Question 61 — Multiple Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Correct options**: `A, C` |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Correct options**: `A, C` |
| **"without requiring reserved throughput"** | $\rightarrow$ **Correct options**: `A, C` |
| **"variable customer support traffic"** | $\rightarrow$ **Correct options**: `A, C` |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer: AC (Azure OpenAI Embedding & Text Split) Contoso requires an indexing pipeline for Agent1 to retrieve relevant produ...*


---

### 📌 Question 62 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Option C** (Azure AI Search) |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Option C** (Azure AI Search) |
| **"without requiring reserved throughput"** | $\rightarrow$ **Option C** (Azure AI Search) |
| **"variable customer support traffic"** | $\rightarrow$ **Option C** (Azure AI Search) |

> 🧠 **Memory Anchor**: *Technical Justification for Recommending Azure AI Search (Option C) Why Option C (Azure AI Search) is the Best Choice: Meets Technical Requirements: Enables sem...*


---

### 📌 Question 63 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Set the output_content_format=ContentFormat.MARKDOWN value."** | $\rightarrow$ **Option D** (Set the output_content_format=ContentFormat.MARKDOWN value.) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer (D) To configure Azure Document Intelligence in Foundry Tools for generating Markdown output that preserves  the sect...*


---

### 📌 Question 64 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"a custom Azure Content Understanding in Foundry Tools analyzer that defines the required fields as the"** | $\rightarrow$ **Option B** (a custom Azure Content Understanding in Foundry Tools analyzer that defines the required fields as the) |
| **"it directly addresses all specified"** | $\rightarrow$ **Option B** (a custom Azure Content Understanding in Foundry Tools analyzer that defines the required fields as the) |
| **"Groundedness"** | $\rightarrow$ **Option B** (a custom Azure Content Understanding in Foundry Tools analyzer that defines the required fields as the) |
| **"relevance"** | $\rightarrow$ **Option B** (a custom Azure Content Understanding in Foundry Tools analyzer that defines the required fields as the) |

> 🧠 **Memory Anchor**: *Technical Justification for Choosing Option B Why B is the Best Choice:A custom Azure Content Understanding (ACU) in Foundry Tools analyzer, as  described in op...*


---

### 📌 Question 65 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Groundedness Evaluation Metrics is the most suitable choice"** | $\rightarrow$ **Option D** (Groundedness Evaluation Metrics is the most suitable choice, and why the others are less appropriate) |
| **"Evaluation Metrics"** | $\rightarrow$ **Option D** (Groundedness Evaluation Metrics is the most suitable choice, and why the others are less appropriate) |
| **"Groundedness"** | $\rightarrow$ **Option D** (Groundedness Evaluation Metrics is the most suitable choice, and why the others are less appropriate) |
| **"Relevance"** | $\rightarrow$ **Option D** (Groundedness Evaluation Metrics is the most suitable choice, and why the others are less appropriate) |

> 🧠 **Memory Anchor**: *Technical Justification for Correct Answer (D) To address the issue of decreased accuracy in the agent's responses after a content update in a Microsoft  Foundr...*


---

### 📌 Question 66 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Correct option**: `A` |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Correct option**: `A` |
| **"without requiring reserved throughput"** | $\rightarrow$ **Correct option**: `A` |
| **"variable customer support traffic"** | $\rightarrow$ **Correct option**: `A` |

---

### 📌 Question 67 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Option B** (memory) |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Option B** (memory) |
| **"without requiring reserved throughput"** | $\rightarrow$ **Option B** (memory) |
| **"variable customer support traffic"** | $\rightarrow$ **Option B** (memory) |

---

### 📌 Question 68 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"To ensure that the `Agent1Dev Team` (represented by the security group `SC_Agent1_Dev`) can access 
`Project1` within Microsoft Foundry using Microsoft Entra authentication, you must assign the appropriate role 
to the security group at the project scope.Based on standard Azure AI/Foundry role-based access control 
(RBAC) patterns for developers:1. Role Assignment: The role required to access and manage a project is"** | $\rightarrow$ **Answer**: `To ensure that the `Agent1Dev Team` (represented by the security group `SC_Agent1_Dev`) can access 
`Project1` within Microsoft Foundry using Microsoft Entra authentication, you must assign the appropriate role 
to the security group at the project scope.Based on standard Azure AI/Foundry role-based access control 
(RBAC) patterns for developers:1. Role Assignment: The role required to access and manage a project is` |
| **"data processed by the model must remain within the EU"** | $\rightarrow$ **Answer**: `To ensure that the `Agent1Dev Team` (represented by the security group `SC_Agent1_Dev`) can access 
`Project1` within Microsoft Foundry using Microsoft Entra authentication, you must assign the appropriate role 
to the security group at the project scope.Based on standard Azure AI/Foundry role-based access control 
(RBAC) patterns for developers:1. Role Assignment: The role required to access and manage a project is` |
| **"remain consistent to ensure stable responses"** | $\rightarrow$ **Answer**: `To ensure that the `Agent1Dev Team` (represented by the security group `SC_Agent1_Dev`) can access 
`Project1` within Microsoft Foundry using Microsoft Entra authentication, you must assign the appropriate role 
to the security group at the project scope.Based on standard Azure AI/Foundry role-based access control 
(RBAC) patterns for developers:1. Role Assignment: The role required to access and manage a project is` |
| **"without requiring reserved throughput"** | $\rightarrow$ **Answer**: `To ensure that the `Agent1Dev Team` (represented by the security group `SC_Agent1_Dev`) can access 
`Project1` within Microsoft Foundry using Microsoft Entra authentication, you must assign the appropriate role 
to the security group at the project scope.Based on standard Azure AI/Foundry role-based access control 
(RBAC) patterns for developers:1. Role Assignment: The role required to access and manage a project is` |

---

### 📌 Question 69 — Multiple Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Retrieval Augmented Generation"** | $\rightarrow$ **Correct options**: `A, D` |
| **"Groundedness"** | $\rightarrow$ **Correct options**: `A, D` |
| **"Retrieval"** | $\rightarrow$ **Correct options**: `A, D` |
| **"A, D"** | $\rightarrow$ **Correct options**: `A, D` |

---

### 📌 Question 70 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"conversation"** | $\rightarrow$ **Option C** (conversation) |

---

### 📌 Question 71 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Groundedness, Relevance, Protected Material Detection"** | $\rightarrow$ **Answer**: `Groundedness, Relevance, Protected Material Detection` |
| **"evaluation metrics"** | $\rightarrow$ **Answer**: `Groundedness, Relevance, Protected Material Detection` |
| **"Answer"** | $\rightarrow$ **Answer**: `Groundedness, Relevance, Protected Material Detection` |

---

### 📌 Question 72 — Multiple Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"risk and safety metrics"** | $\rightarrow$ **Correct options**: `A, E` |
| **"Option E (Visual Block"** | $\rightarrow$ **Correct options**: `A, E` |
| **"A, E"** | $\rightarrow$ **Correct options**: `A, E` |

---

### 📌 Question 73 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option A (Visual Block"** | $\rightarrow$ **Option A** (Option A (Visual Block)) |

---

### 📌 Question 74 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Increase the temperature parameter."** | $\rightarrow$ **Option C** (Increase the temperature parameter.) |

---

### 📌 Question 75 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option D (Visual Block"** | $\rightarrow$ **Option D** (Option D (Visual Block)) |

---

### 📌 Question 77 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"session"** | $\rightarrow$ **session_id**: `user_id`, **storage_type**: `session` |
| **"user_id"** | $\rightarrow$ **session_id**: `user_id`, **storage_type**: `session` |

---

### 📌 Question 78 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Route requests through the Azure OpenAI endpoint."** | $\rightarrow$ **Option C** (Route requests through the Azure OpenAI endpoint.) |
| **"Content Safety"** | $\rightarrow$ **Option C** (Route requests through the Azure OpenAI endpoint.) |

---

### 📌 Question 79 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Ask for approval / Ask a question node"** | $\rightarrow$ **Workflow logic**: `Condition/decision branch for risk`, **Approval checkpoint**: `Ask for approval / Ask a question node` |
| **"Condition/decision branch for risk"** | $\rightarrow$ **Workflow logic**: `Condition/decision branch for risk`, **Approval checkpoint**: `Ask for approval / Ask a question node` |

---

### 📌 Question 80 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option D (Visual Block"** | $\rightarrow$ **Option D** (Option D (Visual Block)) |

---

### 📌 Question 81 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option B (Visual Block"** | $\rightarrow$ **Option B** (Option B (Visual Block)) |

---

### 📌 Question 82 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option A (Visual Block"** | $\rightarrow$ **Option A** (Option A (Visual Block)) |

---

### 📌 Question 83 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"semantic search only"** | $\rightarrow$ **Option B** (semantic search only) |

---

### 📌 Question 84 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"GenAI Prompt"** | $\rightarrow$ **Option B** (GenAI Prompt) |

---

### 📌 Question 85 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Image Analysis"** | $\rightarrow$ **Option C** (Image Analysis) |

---

### 📌 Question 86 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Describe the color scheme of the video segment"** | $\rightarrow$ **Field value type**: `string`, **Field method**: `generate`, **Prompt**: `Describe the color scheme of the video segment` |
| **"generate"** | $\rightarrow$ **Field value type**: `string`, **Field method**: `generate`, **Prompt**: `Describe the color scheme of the video segment` |
| **"string"** | $\rightarrow$ **Field value type**: `string`, **Field method**: `generate`, **Prompt**: `Describe the color scheme of the video segment` |

---

### 📌 Question 87 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"a multiple-file task in pro mode that uses the vendor contract files as reference data"** | $\rightarrow$ **Option C** (a multiple-file task in pro mode that uses the vendor contract files as reference data) |

---

### 📌 Question 88 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Apply a mask-based inpainting edit to the affected part of the video."** | $\rightarrow$ **Option D** (Apply a mask-based inpainting edit to the affected part of the video.) |

---

### 📌 Question 89 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Set the user message content array to include items that have type: text and type: image_url"** | $\rightarrow$ **Option A** (Set the user message content array to include items that have type: text and type: image_url.) |

---

### 📌 Question 90 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"WebSocket"** | $\rightarrow$ **Option D** (WebSocket) |

---

### 📌 Question 91 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Set project-endpoint to the endpoint of the project."** | $\rightarrow$ **Option A** (Set project-endpoint to the endpoint of the project.) |

---

### 📌 Question 92 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"principle of least privilege"** | $\rightarrow$ **Answer**: `Managed` |
| **"Managed"** | $\rightarrow$ **Answer**: `Managed` |
| **"Answer"** | $\rightarrow$ **Answer**: `Managed` |

---

### 📌 Question 93 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Yes"** | $\rightarrow$ **Can detect custom objects without model deployment**: `Yes`, **Can extract structured JSON from unstructured text**: `No`, **Can preserve document layout and table bounds**: `Yes` |
| **"No"** | $\rightarrow$ **Can detect custom objects without model deployment**: `Yes`, **Can extract structured JSON from unstructured text**: `No`, **Can preserve document layout and table bounds**: `Yes` |
| **"Yes"** | $\rightarrow$ **Can detect custom objects without model deployment**: `Yes`, **Can extract structured JSON from unstructured text**: `No`, **Can preserve document layout and table bounds**: `Yes` |

---

### 📌 Question 94 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Custom dimensions"** | $\rightarrow$ **Telemetry tracking signal 1**: `Trace context`, **Telemetry tracking signal 2**: `Custom dimensions` |
| **"tool invocation"** | $\rightarrow$ **Telemetry tracking signal 1**: `Trace context`, **Telemetry tracking signal 2**: `Custom dimensions` |
| **"Trace context"** | $\rightarrow$ **Telemetry tracking signal 1**: `Trace context`, **Telemetry tracking signal 2**: `Custom dimensions` |

---

### 📌 Question 95 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Validate file size against model limits before upload"** | $\rightarrow$ **HTTP 429 Error Resolution**: `Implement exponential backoff retry logic`, **HTTP 400 Error Resolution**: `Validate file size against model limits before upload` |
| **"Implement exponential backoff retry logic"** | $\rightarrow$ **HTTP 429 Error Resolution**: `Implement exponential backoff retry logic`, **HTTP 400 Error Resolution**: `Validate file size against model limits before upload` |
| **"Azure OpenAI"** | $\rightarrow$ **HTTP 429 Error Resolution**: `Implement exponential backoff retry logic`, **HTTP 400 Error Resolution**: `Validate file size against model limits before upload` |
| **"rate limit"** | $\rightarrow$ **HTTP 429 Error Resolution**: `Implement exponential backoff retry logic`, **HTTP 400 Error Resolution**: `Validate file size against model limits before upload` |

---

### 📌 Question 96 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option A (Visual Block"** | $\rightarrow$ **Option A** (Option A (Visual Block)) |

---

### 📌 Question 97 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option D (Visual Block"** | $\rightarrow$ **Option D** (Option D (Visual Block)) |

---

### 📌 Question 98 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"resource connection 
'Microsoft.MachineLearningServices/workspaces/onlineEndpoints/deployments/connections@2024-01-01-
preview' = name: 'KV1-connection' parent: deployment properties: category: 'AzureKeyVault' target: 
kv1.properties.vaultUri authType: 'None"** | $\rightarrow$ **Answer**: `resource connection 
'Microsoft.MachineLearningServices/workspaces/onlineEndpoints/deployments/connections@2024-01-01-
preview' = name: 'KV1-connection' parent: deployment properties: category: 'AzureKeyVault' target: 
kv1.properties.vaultUri authType: 'None'` |
| **"Answer"** | $\rightarrow$ **Answer**: `resource connection 
'Microsoft.MachineLearningServices/workspaces/onlineEndpoints/deployments/connections@2024-01-01-
preview' = name: 'KV1-connection' parent: deployment properties: category: 'AzureKeyVault' target: 
kv1.properties.vaultUri authType: 'None'` |

---

### 📌 Question 99 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"For the requirements of grounding responses in specific company policy documents and retaining customer"** | $\rightarrow$ **Answer**: `For the requirements of grounding responses in specific company policy documents and retaining customer` |
| **"Answer"** | $\rightarrow$ **Answer**: `For the requirements of grounding responses in specific company policy documents and retaining customer` |

---

### 📌 Question 100 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Add a retry evaluation before the responses are returned."** | $\rightarrow$ **Option A** (Add a retry evaluation before the responses are returned.) |

---

### 📌 Question 101 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Yes"** | $\rightarrow$ **Vision API detects brand logos in images**: `Yes`, **Returns confidence scores for brand detection**: `Yes`, **Requires pre-training custom vision model**: `No` |
| **"Yes"** | $\rightarrow$ **Vision API detects brand logos in images**: `Yes`, **Returns confidence scores for brand detection**: `Yes`, **Requires pre-training custom vision model**: `No` |
| **"No"** | $\rightarrow$ **Vision API detects brand logos in images**: `Yes`, **Returns confidence scores for brand detection**: `Yes`, **Requires pre-training custom vision model**: `No` |

---

### 📌 Question 102 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option C (Visual Block"** | $\rightarrow$ **Option C** (Option C (Visual Block)) |

---

### 📌 Question 103 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"A, C"** | $\rightarrow$ **Correct options**: `A, C` |

---

### 📌 Question 104 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Content Safety"** | $\rightarrow$ **Correct options**: `A, D` |
| **"A, D"** | $\rightarrow$ **Correct options**: `A, D` |

---

### 📌 Question 105 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Replace ContactInfo by using Phone"** | $\rightarrow$ **Option D** (Replace ContactInfo by using Phone, Email, and SocialMedia entities. Relabel every matching span.) |

---

### 📌 Question 106 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Use Speech Synthesis Markup Language (SSML) to adjust the prosody of the voice."** | $\rightarrow$ **Option B** (Use Speech Synthesis Markup Language (SSML) to adjust the prosody of the voice.) |

---

### 📌 Question 107 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Yes"** | $\rightarrow$ **Redacts PII before sending prompt to model**: `Yes`, **Stores unmasked PII in Application Insights**: `No`, **Preserves original sentence context for model**: `Yes` |
| **"No"** | $\rightarrow$ **Redacts PII before sending prompt to model**: `Yes`, **Stores unmasked PII in Application Insights**: `No`, **Preserves original sentence context for model**: `Yes` |
| **"Yes"** | $\rightarrow$ **Redacts PII before sending prompt to model**: `Yes`, **Stores unmasked PII in Application Insights**: `No`, **Preserves original sentence context for model**: `Yes` |

---

### 📌 Question 108 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Train and publish the model"** | $\rightarrow$ **Step 1**: `Create a project`, **Step 2**: `Upload and tag images`, **Step 3**: `Train and publish the model` |
| **"Upload and tag images"** | $\rightarrow$ **Step 1**: `Create a project`, **Step 2**: `Upload and tag images`, **Step 3**: `Train and publish the model` |
| **"Create a project"** | $\rightarrow$ **Step 1**: `Create a project`, **Step 2**: `Upload and tag images`, **Step 3**: `Train and publish the model` |

---

### 📌 Question 109 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option B (Visual Block"** | $\rightarrow$ **Option B** (Option B (Visual Block)) |

---

### 📌 Question 110 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Option C (Visual Block"** | $\rightarrow$ **Option C** (Option C (Visual Block)) |

---

### 📌 Question 111 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"the endpoint URI and subscription key"** | $\rightarrow$ **Option A** (the endpoint URI and subscription key) |

---

### 📌 Question 112 — Drag Drop

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"E, B, D"** | $\rightarrow$ **Correct options**: `E, B, D` |

---

### 📌 Question 113 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"AI Services"** | $\rightarrow$ **Answer**: `AI Services` |
| **"Answer"** | $\rightarrow$ **Answer**: `AI Services` |

---

### 📌 Question 114 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"The provided images show a graph where the x-axis represents the number of training iterations and the y-
axis represents the loss (specifically, the training loss and validation loss). Based on the standard 
interpretation of such machine learning performance graphs:* Statement 1: The model is experiencing 
overfitting (because the training loss continues to decrease while the validation loss begins to 
increase/plateau).* Statement 2: To improve the model performance, you should increase the amount of 
training data or apply regularization (which prevents the model from memorizing the noise in the training 
set).Based on the typical structure of this specific certification exam question (AI-103/AI-102 context), the 
correct selections are:OverfittingIncrease the amount of training data"** | $\rightarrow$ **Answer**: `The provided images show a graph where the x-axis represents the number of training iterations and the y-
axis represents the loss (specifically, the training loss and validation loss). Based on the standard 
interpretation of such machine learning performance graphs:* Statement 1: The model is experiencing 
overfitting (because the training loss continues to decrease while the validation loss begins to 
increase/plateau).* Statement 2: To improve the model performance, you should increase the amount of 
training data or apply regularization (which prevents the model from memorizing the noise in the training 
set).Based on the typical structure of this specific certification exam question (AI-103/AI-102 context), the 
correct selections are:OverfittingIncrease the amount of training data` |
| **"Answer"** | $\rightarrow$ **Answer**: `The provided images show a graph where the x-axis represents the number of training iterations and the y-
axis represents the loss (specifically, the training loss and validation loss). Based on the standard 
interpretation of such machine learning performance graphs:* Statement 1: The model is experiencing 
overfitting (because the training loss continues to decrease while the validation loss begins to 
increase/plateau).* Statement 2: To improve the model performance, you should increase the amount of 
training data or apply regularization (which prevents the model from memorizing the noise in the training 
set).Based on the typical structure of this specific certification exam question (AI-103/AI-102 context), the 
correct selections are:OverfittingIncrease the amount of training data` |

---

### 📌 Question 115 — Multiple Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Supply the groups as a filter for the search requests"** | $\rightarrow$ **Correct options**: `A, E, F` |
| **"Retrieve the group memberships of the user"** | $\rightarrow$ **Correct options**: `A, E, F` |
| **"Add allowed groups to each index entry"** | $\rightarrow$ **Correct options**: `A, E, F` |
| **"A, E, F"** | $\rightarrow$ **Correct options**: `A, E, F` |

---

### 📌 Question 116 — Single Choice

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Azure Content Understanding"** | $\rightarrow$ **Option C** (Azure Content Understanding) |

---

### 📌 Question 117 — Hotspot

| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |
| :--- | :--- |
| **"Object projection"** | $\rightarrow$ **JSON data projection type**: `Object projection`, **Extracted text data projection type**: `Table projection` |
| **"Table projection"** | $\rightarrow$ **JSON data projection type**: `Object projection`, **Extracted text data projection type**: `Table projection` |

---
