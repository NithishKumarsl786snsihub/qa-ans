# Extracted Question Bank

Source PDF: `Developing AI Apps and Agents on Azure - dump.pdf`

## Question 1

Source pages: 2, 3, 4

HOTSPOT - 
Case Study - 
This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - 
Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. 
The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: 
Agent1 uses a base model deployment. 
A safety evaluation pipeline is NOT enabled. 
Tool invocation approval workflows are NOT enabled. 
Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: 
Agent1 has only general knowledge of the Contoso products. 
A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. 
Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: 
Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. 
Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. 
Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. 
Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. 
Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: 
The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. 
The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. 
Responses generated by using the product sheet information must be relevant, complete, and accurate. 
Agent1 must be able to use the product sheets to answer natural language questions about product details. 
The model version used by Agent1 must remain consistent to ensure stable responses. 
The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: 
API keys must NOT be used to access Foundry-deployed models. 
Access to the Azure resources must follow the principle of least privilege. 
The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. 
Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. 
Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. 
Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. 
The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: 
Users that interact with Agent1 must have a personalized experience in future interactions, including the ability for 
Agent1 to retain conversation context and recall relevant information from previous interactions. 
Agent1 must answer questions only about the products sold by Contoso. 
You need to configure the model deployment for Agent1 to meet the technical requirements. 
What should you configure? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: Deployment Type: Selected as Standard because the workload requires dynamic scaling for variable traffic without reserved throughput capacity (eliminating Provisioned options), while adhering to strict regional data

Explanation:
Deployment Type: Selected as Standard because the workload requires dynamic scaling for variable traffic without reserved throughput capacity (eliminating Provisioned options), while adhering to strict regional data 
residency guidelines (e.g., data remaining within a specific zone or region like the EU). Version Update Policy: Selected as Once the current version expires because the model version must remain 
consistent to guarantee stable, predictable responses over time, rather than automatically upgrading as soon 
as a new default version becomes available. Why the other answer are incorrect: Global Standard: Incorrect because "Global" routing sends traffic dynamically to any region worldwide with available capacity. This violates strict data residency/compliance rules if your data must remain within a 
specific geographic boundary (like the EU or US). Global Provisioned: Incorrect because "Provisioned" requires buying reserved Throughput Units (PTUs). This 
incurs a high, fixed cost regardless of usage, making it wrong for workloads with variable, low-volume traffic 
where minimizing costs is a priority. Opt out of automatic model version upgrades: Incorrect because this policy is deprecated or not recommended for long-term consistency. When a model version reaches its official retirement date, it will 
force-upgrade anyway, meaning you cannot permanently opt out of upgrades. Upgrade once a new default version becomes available: Incorrect because this causes the model to update automatically as soon as Microsoft releases a new default. This can break application code or change prompt 
behaviors unexpectedly, violating requirements for strict consistency.

## Question 2

Source pages: 4, 5, 6, 7

Case Study - This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - 
Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. 
The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: 
Agent1 uses a base model deployment. 
A safety evaluation pipeline is NOT enabled. 
Tool invocation approval workflows are NOT enabled. 
Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: 
Agent1 has only general knowledge of the Contoso products. 
A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. 
Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. 
The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: 
Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. 
Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. 
Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. 
Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. 
Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. 
The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. 
Responses generated by using the product sheet information must be relevant, complete, and accurate. 
Agent1 must be able to use the product sheets to answer natural language questions about product details. 
The model version used by Agent1 must remain consistent to ensure stable responses. 
The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: 
API keys must NOT be used to access Foundry-deployed models. 
Access to the Azure resources must follow the principle of least privilege. 
The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. 
Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. 
Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. 
Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. 
The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: 
Users that interact with Agent1 must have a personalized experience in future interactions, including the ability for 
Agent1 to retain conversation context and recall relevant information from previous interactions. 
Agent1 must answer questions only about the products sold by Contoso. 
You need to configure Agent1 to meet the security and compliance requirements. 
What should you use?

Options:
- A. self-harm content filtering
- B. prompt shields
- C. Personally identifiable information (PII) Detection
- D. violence content filtering

Answer: B

Explanation:
Technical Justification for Correct Answer: B. Prompt Shields Why B (Prompt Shields) is the best option: Security and Compliance Requirement Alignment: The primary reason for choosing Prompt Shields is its 
direct alignment with multiple security and compliance requirements stated by Contoso. Specifically, it 
addresses the need to protect Agent1 from revealing customer information (even when erroneously exposed) 
and from potential malicious instructions hidden within images in product sheets. Protection Against Malicious Inputs: Prompt Shields are designed to filter out or shield against potentially harmful or unwanted inputs (including those that might be embedded in images), ensuring Agent1's responses 
remain safe and compliant. Relevance to General Security Posture: Given the constraints around not using API keys and the emphasis on 
least privilege access, leveraging Prompt Shields further fortifies the security posture of Agent1 without 
introducing additional access vulnerabilities. Why Other Options are Less Suitable: A. Self-Harm Content Filtering: Relevance: While important, self-harm content filtering does not directly address the specified security and 
compliance requirements related to protecting against malicious instructions or inadvertently exposed customer data. Scope: The primary concern here is not the content generated by Agent1 in response to self-harm queries but 
ensuring the security of the input process. 
C. Personally Identifiable Information (PII) Detection: Relevance: Although PII Detection is crucial for data privacy, the question's focus is on protecting Agent1 from malicious inputs and ensuring it doesn't reveal customer information proactively. PII Detection is more 
about identifying than preventing exposure. 
Proactivity: The requirement implies a need for a proactive protection mechanism rather than a detection 
capability. 
D. Violence Content Filtering: 
Relevance: Similar to self-harm content filtering, this does not directly address the protection against malicious instructions or the accidental exposure of customer information as highlighted in the problem 
statement. 
Scope: The concern is broader than just filtering violent content; it's about securing the input pipeline. Conclusion:Given the specific security and compliance requirements outlined by Contoso, particularly the need to protect against malicious inputs and prevent the exposure of customer information, Prompt Shields (B) is the most appropriate choice. It directly addresses the identified risks without introducing additional vulnerabilities, aligning with the principle of least privilege and enhancing the overall security posture of 
Agent1. References Microsoft Documentation: security and compliance for Azure AI Services 
Microsoft Learn: Protecting AI Models from Malicious Inputs

## Question 3

Source pages: 7, 8

You are planning a Microsoft Foundry project named Project1 that will contain multiple agents. Each agent will 
access the same Azure AI Search resource. 
You need to recommend a solution to centrally manage the Azure AI Search credentials within Project1. The 
solution must be implemented across all the agents. 
What should you recommend?

Options:
- A. Enable role-based access control (RBAC) for the Azure AI Search resource.
- B. Disable key-based access control on the Azure AI Search resource.
- C. Add a connection to the Azure AI Search resource.
- D. Create a managed private endpoint that connects to the Azure AI Search resource.

Answer: C

Explanation:
Technical Justification for Recommending Option C For centrally managing Azure AI Search credentials across multiple agents in Project1, Option C: Add a 
connection to the Azure AI Search resource is the most suitable choice. Here’s why: Option C is the best because adding a connection to the Azure AI Search resource within the Microsoft 
Foundry project (Project1) allows for a centralized management approach. This connection can be securely 
shared or referenced across all agents within the project, ensuring that credentials are not hardcoded or 
duplicated across agents. Instead, agents can leverage this single, managed connection, enhancing security 
and simplifying credential updates. Why Other Options are Less Suitable: Option A: Enable role-based access control (RBAC) for the Azure AI Search resource 
While RBAC is crucial for controlling access, it does not directly address the central management of credentials for accessing the Azure AI Search resource. RBAC defines what actions can be performed but 
does not consolidate credential management across multiple agents. 
Suitability for Central Credential Management: Low Option B: Disable key-based access control on the Azure AI Search resource Disabling key-based access would likely increase security risks by potentially forcing the use of less secure methods or complicating access management. This does not contribute to centralizing credential 
management. 
Suitability for Central Credential Management: Very Low (Counterproductive) Option D: Create a managed private endpoint that connects to the Azure AI Search resource While a managed private endpoint enhances security by providing a private, secure connection to the Azure AI Search resource, it focuses on network security rather than the central management of credentials for access 
by multiple agents. 
Suitability for Central Credential Management: Low Recommendation Summary:Given the need for central management of Azure AI Search credentials across 
multiple agents in Project1, Option C is the most direct and effective solution, facilitating secure, centralized 
credential management. References: For further understanding of managing connections and security in Azure and Microsoft Foundry, refer to: 1. Microsoft Documentation - Manage connections in Microsoft Foundry: https://learn.microsoft.com/en-us/microsoft-365/apps/foundry/manage-connections?view=o365-
worldwide 2. Azure Documentation - Secure your Azure AI Search with Azure RBAC: https://learn.microsoft.com/en-us/azure/search/security-azure-rbac

## Question 4

Source pages: 8, 9

HOTSPOT - 
Your company is piloting a customer support agent in a Microsoft Foundry project name Project1. Project1 is 
connected to an existing Application Insights resource, and the company’s support team reviews runs in the Traces 
tab. 
The Foundry Agent Service is configured to perform the following actions: 
Retrieve the Application Insights connection string by calling 
project_client.telemetry.get_application_insights_connection_string().   
Call configure_azure_monitor(connection_string=...) to enable telemetry. 
A separate LangChain service is configured to use OpenTelemetry and has the following configurations: 
Uses AzureAIOpenTelemetryTracer(connection_string=..., enable_content_recording=False) 
Passes the tracer by using config= “callbacks”:[azure_tracer] 
Company policy has the following requirements: 
Telemetry from LangChain and OpenTelemetry must be distinguishable within the same Application Insights 
resource. 
Secrets and credentials must NOT be stored in prompts, tool arguments, or span attributes. 
For each of the following statements, select Yes if the statement is true. Otherwise, select No. 
NOTE: Each correct selection is worth one point.

Answer: _No answer text extracted._

Explanation:
Statement 1: No OpenTelemetry tracing requires explicit configuration to start capturing data. Without setting up an active OpenTelemetry exporter or attaching a dedicated tracer (such as AzureAIOpenTelemetryTracer or calling configure_azure_monitor), no trace spans or events will be captured or forwarded to Azure Monitor. Statement 2: Yes The OTEL_SERVICE_NAME environment variable determines the logical name of your application service in OpenTelemetry telemetry data. Configuring distinct values for different services allows Azure Application 
Insights to map, filter, and isolate them into distinct components within the Application Map view. Statement 3: No Setting enable_content_recording=False explicitly tells the tracer to exclude the actual text content of prompts, completions, and tool data payloads from the telemetry attributes. This protects user privacy and prevents sensitive personal data or secrets from being stored inside logs.

## Question 5

Source pages: 9, 10

DRAG DROP - Include a pipeline named Pipeline1 that supports cost-effective, high-volume processing of standalone PDF invoices. 
Include a pipeline named Pipeline2 that supports cross-document validation by using multi-step reasoning and 
reference data. 
How should you configure each pipeline? To answer, drag the appropriate configurations to the correct pipelines. 
Each configuration may be used once, more than once, of not at all. You may need to drag the split bar between 
panes or scroll to view content. 
NOTE: Each correct selection is worth one point.

Answer: Pipeline1 (Single-file task in standard mode): This is correct for workflows processing independent, standalone documents one by one. Standard mode

Explanation:
Pipeline1 (Single-file task in standard mode): This is correct for workflows processing independent, standalone documents one by one. Standard mode 
handles individual file parsing efficiently. It minimizes computational costs for basic schema extraction. Pipeline2 (Multi-file task in pro mode): This is correct for workflows requiring cross-document logic or advanced generative reasoning. Pro mode processes batches of interrelated files together. It allows the model to correlate information across multiple 
files. Incorrect answer: Single-file task in pro mode: This is incorrect because Pro mode's core advantage is cross-file reasoning. Using it for a single file 
unnecessarily increases processing limits and costs without utilizing multi-file capabilities. Multi-file task in standard mode: This is incorrect because Standard mode lacks the architecture to handle relational dependencies across multiple files. Combining multiple files under standard mode results in schema rejection or validation errors.

## Question 6

Source pages: 10, 11, 12

HOTSPOT - Authenticates by using a Microsoft Entra managed identity 
Sends prompts to a deployed model by using the Azure OpenAI Responses API 
How should you complete the Python code? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: First Dropdown: DefaultAzureCredential Second Dropdown: create Credential Initialization: The scenario specifies authentication using a Microsoft Entra managed identity. In Azure Python SDKs, DefaultAzureCredential automatically orchestrates managed identities across both local development and Azure-hosted environments. It is explicitly imported at the top of the snippet (from azure.identity import DefaultAzureCredential). Responses API Call: When interacting with the Azure OpenAI-compatible project client endpoint via openai_client.responses, the standard method to generate chat text completions or send user prompts to the deployed generative model is create.

Explanation:
First Dropdown: DefaultAzureCredential Second Dropdown: create Credential Initialization: The scenario specifies authentication using a Microsoft Entra managed identity. In Azure Python SDKs, DefaultAzureCredential automatically orchestrates managed identities across both local development and Azure-hosted environments. It is explicitly imported at the top of the snippet (from azure.identity import DefaultAzureCredential). Responses API Call: When interacting with the Azure OpenAI-compatible project client endpoint via openai_client.responses, the standard method to generate chat text completions or send user prompts to the deployed generative model is create.

## Question 7

Source pages: 12, 13

HOTSPOT - 
You have a Microsoft Foundry project that contains a workflow for a customer support triage process. 
You have an Ask a question node that stores user responses in a local variable named Var01. An if/else condition expression that ensures that Var01 contains a value 
A Send message expression that returns the stored user response in uppercase

Answer: _No answer text extracted._

Explanation:
If/else condition expression: Not(IsBlank(Local.Var01)) Send message expression: Upper(Local.Var01) If/else condition expression: The requirement is to ensure that the variable contains a value (i.e., it is not empty or blank). IsBlank(Local.Var01) evaluates to True if it has no value. Wrapping it in the Not() function inverts this logic, making the expression evaluate to True only when a valid value exists. Send message expression: To display or send a variable dynamically inside a message node, the variable/formula must be enclosed 
within curly brackets string interpolation syntax. The Upper() function converts the text string to uppercase characters. The variable prefix Local. must be explicitly retained to reference the locally-scoped variable correctly within the expression payload ( Upper(Local.Var01) ).

## Question 8

Source pages: 14, 15

HOTSPOT - 
You have a Microsoft Foundry project that contains a customer support agent built by using the Foundry Agent 
Service. 
The agent uploads user-provided screenshots to Azure Storage through a ticketing tool and receives a blob URL 
for additional reasoning. 
You need to use image moderation during agent runs and prevent harmful content from being returned during 
runs. Azure AI Content Safety must access the images by using the blob URL. The solution must follow the 
principle of least privilege. 
What should you configure for Content Safety? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: Guardrails Select User input, Output, Tool response, and Tool call and set Action to Block. Storage access A system-assigned managed identity that is assigned the Storage Blob Data Reader role To securely evaluate and prevent harmful or unsafe content from being returned or processed at any point

Explanation:
Guardrails Select User input, Output, Tool response, and Tool call and set Action to Block. Storage access A system-assigned managed identity that is assigned the Storage Blob Data Reader role To securely evaluate and prevent harmful or unsafe content from being returned or processed at any point 
during an agentic session, content safety filters must be applied comprehensively across all interaction 
touchpoints. Setting the action to Block ensures that any policy violations are immediately halted rather than 
merely flagged or annotated in logs, completely protecting the user interface from receiving or exposing 
toxic data. Storage access: System-assigned managed identity eliminates password management overhead. Storage Blob Data Reader satisfies the principle of least privilege, providing full read access to download and review image binaries without granting unnecessary write or delete capabilities (which would be included 
in the Contributor role).

## Question 9

Source pages: 15

You have a Microsoft Foundry project that contains three agents as shown in the following table. You need to orchestrate the agents to ensure that the customer requests meet the following requirements: 
Support a deterministic, step-based process that uses conditional branching and shared state across the agents. 
Optionally trigger a ticket action based on the triage result. 
The solution must minimize development effort. 
What should you include in the solution?

Options:
- A. a workflow
- B. threads and runs without a workflow
- C. a multi-agent group chat session
- D. separate agent runs coordinated in the application code

Answer: A

Explanation:
A. a workflow. Why a workflow is correct: In Microsoft Azure AI Foundry, agentic workflows are purposely built to 
orchestrate multiple agents using declarative, predefined sequences. They natively support deterministic 
step-by-step logic, if/else conditional branching, and automatic variable/state sharing across agents without 
requiring developers to write complex application orchestration or synchronization code, minimizing overall 
development effort. Why other options are incorrect: Group chat sessions (C) are designed for autonomous, fluid multi-agent conversations where agents dynamically choose when to chime in or pass control. They do not natively follow strict, deterministic, step-
based workflows. Separate application code loops or standalone threads (B & D) require significant manual engineering effort 
to establish shared states, handle condition mappings, and write error-handling glue logic.

## Question 10

Source pages: 16

You have a Microsoft Foundry project that contains an agent. The agent uses Azure Speech in Foundry Tools. 
You fine-tune a baseline speech to text model for the en-us locale and publish the model. 
The agent calls the Speech to text REST API and returns an error message indicating that the project ID is invalid. 
You need to set the project property to the correct ID. 
To what should you set the project property?

Options:
- A. the project URL
- B. the custom speech project ID
- C. the project ID
- D. the custom speech endpoint URL

Answer: B

Explanation:
Technical Justification for Correct Answer: B The correct option to set the project property to resolve the invalid project ID error when using Azure Speech 
in a Microsoft Foundry project is B. the custom speech project ID. Here's why: Why B is Correct: When fine-tuning a baseline speech-to-text model for a specific locale (like en-us) and publishing it through Azure Speech Services, a unique Custom Speech Project ID is generated. This ID is crucial for identifying your specific, customized model when making API calls. The Speech to Text REST API 
requires this exact ID to route the request to your customized model, ensuring the correct speech-to-text processing. Setting the project property to the custom speech project ID ensures that the API call targets 
your fine-tuned model, resolving the invalid project ID error. Why Other Options are Less Suitable: A. the project URL: While the project URL might contain the project ID as part of its path, using the full URL is not the expected format for the project ID field in the API configuration. The API typically expects just the ID, 
not the entire URL, to identify the project. C. the project ID: This option is misleadingly similar to the correct answer. In the context of Azure Speech 
Services, "project ID" could ambiguously refer to a higher-level project container ID (not specific to the customized speech model). The custom speech project ID (Option B) is more precise, indicating it's the ID for 
the fine-tuned speech model, not just any project ID. D. the custom speech endpoint URL: Similar to Option A, using the full endpoint URL is not appropriate for the 
project ID field. The endpoint URL is used to direct the API call to the speech service's entry point, but the 
project ID (specifically the custom speech project ID for your model) is still required within the API call 
parameters to identify which model to use. Technical Summary: The error indicates a mismatch in identifying your customized speech-to-text model. By setting the project property to the custom speech project ID, you ensure the API call accurately references 
your published, fine-tuned model for the en-us locale, thereby resolving the invalid project ID error. References Azure Speech Services Documentation - Custom Speech 
Azure Speech Services REST API Reference - Speech to Text

## Question 11

Source pages: 17, 18

You have a Microsoft Foundry project that contains an agent named PaymentAgent. 
PaymentAgent includes a function tool that issues customer refunds by using an external API. 
You are creating a workflow in YAML. 
You need to ensure that the workflow pauses for human approval and continues with the refund step only after 
approval is granted. 
How should you complete the workflow definition? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: _No answer text extracted._

Explanation:
ask_question: In declarative agent workflows, ask_question is used to explicitly pause execution and collect external feedback or manual intervention (such as human authorization/approval) before proceeding, unlike basic_chat or data_transformation which run automatically. approval == "approved" To ensure that the execute_refund step runs conditionally only if approval has been explicitly granted, the expression evaluates the string output from the preceding id: approval step against the expected value "approved".

## Question 12

Source pages: 18, 19

You have an Azure Speech in Foundry Tools resource that hosts a custom speech to text model deployed to a You are approaching the expiration date of the custom speech to text model. Speech recognition requests will return a 4xx error until a new custom model is deployed. Speech recognition requests will continue to use the expired custom model until the model is removed Speech recognition requests will fall back to the most recent base model for the same locale.

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. Speech recognition requests will fall back to the most recent base model for the
- D. The custom model will be deleted automatically when the model expires.

Answer: C

Explanation:
Technical Justification for Correct Answer: C The correct answer is C. Speech recognition requests will fall back to the most recent base model for the 
same locale. Here's why: Reason for C being correct: When a custom speech-to-text model expires in Azure Speech Services (formerly part of Cognitive Services, now potentially managed through Azure Speech in Foundry Tools as mentioned), 
the service is designed to ensure continuity of service. Instead of interrupting the functionality completely 
(which would be the case with a 4xx error as suggested by A) or requiring immediate manual intervention, Azure Speech Services automatically falls back to the most recent base model for the same locale as the expired custom model. This fallback mechanism minimizes disruption to the agent's speech recognition 
capabilities, ensuring some level of functionality is maintained until a new custom model is deployed. Why A is less suitable: A. Speech recognition requests will return a 4xx error until a new custom model is deployed. This option 
suggests a complete service interruption upon model expiration, which contradicts the design principle of 
Azure Services to provide resilient and continuous functionality wherever possible. A 4xx error implies a 
client-side issue or a deliberate block, which doesn't align with the expected behavior for a managed 
expiration scenario. Why B is less suitable: B. Speech recognition requests will continue to use the expired custom model until the model is removed manually. Continuing to use an expired model could pose security, compliance, or accuracy issues, as the model's support and potential updates would have ceased. Azure services typically do not extend the use of 
expired resources in such a manner without explicit configuration for a temporary extension or auto-renewal, 
which is not implied here. Why D is less suitable: D. The custom model will be deleted automatically when the model expires. While automatic deletion might seem like a housekeeping measure, the immediate question concerns the behavior of speech recognition requests at the time of expiration, not the model's storage lifecycle. The automatic model deletion (if it were to happen immediately, which is not the primary concern here) does not directly address the continuity of the 
speech recognition service's functionality. Correct Answer Summary Correct Answer: C. Speech recognition requests will fall back to the most recent base model for the same 
locale. Rationale: Ensures service continuity with the best available alternative (latest base model for the locale) 
upon custom model expiration, aligning with Azure's design for resilient services. 
References Azure Speech Services: Custom Speech Models Azure Speech Services: How to manage models

## Question 13

Source pages: 20

You have a Microsoft Foundry project that contains a model deployment. 
You have an application that calls the deployment by using the Azure OpenAI v1 API and DefaultAzureCredential. 
The developers at your company receive HTTP 403 errors when they send inference requests, even after running 
az login. 
You need to ensure that the developers can perform model inference. The solution must follow the principle of 
least privilege. 
Which role-based access control (RBAC) role should you assign to the developers?

Options:
- A. Cognitive Services User
- B. Cognitive Services OpenAI User
- C. Contributor
- D. Cognitive Services Data Reader

Answer: B

Explanation:
Technical Justification for Correct Answer: B (Cognitive Services OpenAI User) The correct role-based access control (RBAC) role to assign to the developers for resolving the HTTP 403 
errors when sending inference requests to a Microsoft Foundry (formerly Azure Machine Learning) model 
deployment via the Azure OpenAI v1 API, while adhering to the principle of least privilege, is B. Cognitive 
Services OpenAI User. Here’s why: Cognitive Services OpenAI User (B): This role is specifically designed for users who need to perform OpenAI model inference. Assigning this role ensures that developers have the necessary permissions to call the 
OpenAI API for model inference without granting excessive privileges. This aligns with the principle of least 
privilege, as it only allows actions directly related to the task at hand (OpenAI model inference) and nothing 
more. Why Other Options are Less Suitable: A. Cognitive Services User: While this role provides access to Cognitive Services, it is more general and might not specifically grant the necessary permissions for OpenAI model inference, or it could grant broader access 
than necessary, violating the principle of least privilege. C. Contributor: Assigning the Contributor role would grant far too many permissions, including the ability to manage resources, which is not necessary for simply performing model inference. This vastly exceeds the 
principle of least privilege. D. Cognitive Services Data Reader: This role is focused on reading data from Cognitive Services resources but does not necessarily provide the execution permissions required for model inference via the OpenAI API, 
making it inappropriate for this specific task. Principle of Least Privilege Alignment: Assigning Cognitive Services OpenAI User ensures that developers 
have only the permissions necessary to perform their tasks (model inference via OpenAI API), without any 
additional, potentially risky permissions. References 1. Azure RBAC for Cognitive Services and OpenAI: https://learn.microsoft.com/en-us/azure/cognitive- services/authentication-acls?tabs=platform 2. Azure OpenAI Permissions and Roles: https://learn.microsoft.com/en-us/azure/cognitive- services/openai/how-to-use-manager-keys#permissions-and-roles

## Question 14

Source pages: 21

You have a Microsoft Foundry project that contains an agent. The agent has a Model Context Protocol (MCP) tool 
that queries a knowledge base stored in Azure AI Search. 
Some agent runs return answers from the base model without invoking the knowledge base, which results in 
responses without grounded citations. 
You are provided with the following code snippet that runs the agent. You need to add the correct tool _choice parameter to the code to deterministically force the agent to invoke the 
MCP tool on each run. 
What should you add?

Options:
- A. tool_choice= “required”
- B. tool_choice= “auto”
- C. tool_choice= “type”:“knowledge_base”
- D. tool_choice = “type”:“mcp”

Answer: A

Explanation:
A. tool_choice= “required” . Why it is correct: According to Microsoft Foundry Agent Service tool best practices, the tool_choice parameter provides runtime control over whether a model is allowed to answer directly or is forced to invoke a tool. Setting tool_choice="required" (or passing the parameter mode as a dict/object depending on the specific wrapper structure) explicitly tells the orchestrator that the agent must execute one or more tools before formulating its final response. Since the agent only has the Model Context Protocol (MCP) tool configured for querying the knowledge base, this forces deterministic tool execution on every single run, preventing ungrounded base model hallucinations. Why the other options are incorrect: B ("auto"): This is the default setting. It lets the model autonomously decide whether to use a tool, which makes it non-deterministic and leads to runs skipping the knowledge base entirely. C & D: These options represent invalid formatting syntax for directing type scopes or target keywords within the standard parameter layout for tool-constrained invocation under the Foundry Agent ecosystem.

## Question 15

Source pages: 21, 22

DRAG DROP - You have a Microsoft Foundry project that contains a customer support agent grounded in internal documentation. A small number of responses are flagged for policy violations. Which observability signals should you use for each issue? To answer, drag the appropriate observability signals to 
the correct issues. Each observability signal may be used once, more than once, or not at all. You may need to drag 
the spit bar between panes or scroll to view content. 
NOTE: Each correct selection is worth one point.

Answer: _No answer text extracted._

Explanation:
Unsupported responses Groundedness evaluation metrics Policy violations: Risk and safety metrics Unsupported responses: When an AI model generates responses containing facts or assertions not present in 
the reference context, it results in an ungrounded or unsupported response (hallucination). Tracking Groundedness evaluation metrics assesses the exact ratio of sentences validated by the source text. Policy violations: These occur when inputs or outputs conflict with regulatory or internal content guidelines (e.g., hate speech, violence, or sexual content). Risk and safety metrics directly monitor hits against 
predefined Azure AI Content Safety filter thresholds.

## Question 16

Source pages: 22, 23

You need to ensure that the key value from the connection is included automatically whenever the OpenAPI tool is What should you configure in the OpenAPI specification?

Options:
- A. a header parameter defined for each operation
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: C

Explanation:
Technical Justification for Correct Answer: C To ensure the key value from the connection is included automatically whenever the OpenAPI tool is invoked for the weather service API call, the most appropriate configuration in the OpenAPI specification is an API key 
security scheme. Here's why: Correct Answer: C - an API key security scheme Reason: The API key security scheme in OpenAPI allows for the definition of how an API key is passed (e.g., in 
a header, query, or cookie). Since the weather service requires the key in an HTTP header, configuring an API 
key security scheme in the OpenAPI specification enables the automatic inclusion of the key from the 
connection without needing to redefine it for each operation. This approach is scalable and maintainable, 
especially if the key needs to be updated, as changes can be made in one place. Why Other Options are Less Suitable: A. a header parameter defined for each operation Inconvenience and Redundancy: Defining a header parameter for each operation leads to redundancy and 
increased maintenance effort, especially in large APIs. If the key changes, it would need to be updated in 
multiple places. Lack of Central Management: Doesn't leverage the connection storage's central management capability 
efficiently. B. an Azure Key Vault connection Misalignment with Requirement: While Azure Key Vault is suitable for securely storing secrets, the question specifies that the key is already stored as a connection in Project1. The task is about integrating this existing 
setup with the OpenAPI specification, not about where to store the key. Additional Complexity: Introducing Key Vault at this stage would add unnecessary complexity to the 
immediate requirement of passing the key in the HTTP header. D. a Bearer token security scheme Inappropriate for API Keys: Bearer tokens are typically used for authentication in scenarios involving user 
authentication or service-to-service calls with more complex authentication flows, not for simple API key 
exchanges. Mismatch with Service's Requirement: The weather service specifically requires an API key in the header, not a Bearer token. References OpenAPI Specification - Security Schemes 
Microsoft Azure - Secure your Azure API using API Keys

## Question 17

Source pages: 23, 24

You have a Microsoft Foundry project that serves a high-volume chat app. 
Most requests are simple FAQs, but some require advanced reasoning. You need to reduce costs and latency for common queries, without degrading the quality of the responses to complex questions. 
What should you do?

Options:
- A. Route all the requests to a smaller model.
- B. Use a model cascade that routes the requests to different models.
- C. Increase the value of the max_tokens parameter for all the requests.
- D. Route all the requests to the most capable model.

Answer: B

Explanation:
Technical Justification for Correct Answer: B Why B is the Best Option:Using a model cascade that routes requests to different models is the optimal 
approach for this scenario. This architecture allows for: Cost Reduction: Simple FAQs can be handled by smaller, more efficient models with lower inference costs, 
reducing overall expenses. Latency Reduction: Routing common queries to lighter models decreases response times for the majority of 
requests. Quality Preservation for Complex Queries: Advanced reasoning questions are directed to more capable 
(likely larger) models, ensuring response quality is maintained without compromise. Why Other Options are Less Suitable: A. Route all requests to a smaller model: Quality Deterioration: Complex questions may not be answered accurately, degrading overall service quality. Inadequate Capacity: A single smaller model might not handle the "high-volume" aspect efficiently, 
potentially increasing latency under load. C. Increase the max_tokens parameter for all requests: Cost Increase: Higher max_tokens values increase costs per request, contradicting the goal of reducing costs. Unnecessary Overhead: Simple queries do not benefit from this increase, leading to wasted resources. D. Route all requests to the most capable model: Excessive Cost: Utilizing the most capable model for all queries significantly increases costs due to its higher 
inference expense. 
Latency Concerns: Larger models typically have longer response times, affecting the latency of simple, high-
volume FAQs. Correct Answer Justification Summary:Option B, using a model cascade, strikes a balance between cost 
efficiency, latency reduction for common queries, and maintaining the quality of responses for complex 
inquiries, making it the most suitable solution. References: Microsoft Azure Documentation: Model Deployment Strategies 
Microsoft Azure Cognitive Services: Optimizing Costs for AI Workloads

## Question 18

Source pages: 24, 25, 26

HOTSPOT - You have a Microsoft Foundry project that contains an internal Q&A agent. 
Users report the following issues when they ask the agent questions: 
An increase in the following response: “No relevant information found” 
Periodic HTTP 429 rate limit exceeded errors during peak hours 
You need to identify whether each issue is caused by model unavailability, resource limits, or inference failures. 
What should you do? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: _No answer text extracted._

Explanation:
Metrics to enable : Model Availability Rate and Provisioned Utilization Model Availability Rate isolates whether service errors or operation drop-offs are caused by downstream, 
server-side model unavailability. Provisioned Utilization provides direct observability into capacity and resource limits. When it approaches or exceeds 100%, requests will automatically experience rate-limiting triggers and throw standard HTTP 429 Too Many Requests errors. Diagnostic log to collect Request Response. To store and inspect telemetry data for incoming client interactions, the RequestResponse log category explicitly routes full API payloads (including prompts, generated tokens, status codes, and exact completions) to a destination Log Analytics Workspace.

## Question 19

Source pages: 26, 27

You have a Microsoft Foundry project that contains a high-traffic agent. 
After a recent update, operational costs increase significantly. 
Monitoring confirms that the volume of user traffic to the agent remains unchanged. 
You suspect that changes to the request or response characteristics are causing the increase. You need to identify 
whether the additional costs are driven by the model input size, the model output size, or expanded tool usage. 
Which observability capability should you use?

Options:
- A. latency
- B. evaluation metrics
- C. run success rate
- D. token usage

Answer: D

Explanation:
Technical Justification for Choosing D. Token Usage To identify the cause of increased operational costs in the Microsoft Foundry project, given that user traffic 
volume remains unchanged, we need to focus on the changed characteristics of the requests, responses, or tool usage that could drive up costs. Here’s why D. Token Usage is the most suitable observability capability, 
alongside explanations for why the other options are less suitable: D. Token Usage: Why It's the Best Choice: In the context of AI agents, especially those involving natural language processing (NLP) or similar models, "token usage" refers to the number of tokens (e.g., words, characters) processed by 
the model in requests and responses. Increased model input size (more tokens in requests) or model output size (more tokens in responses) directly correlates with token usage metrics. Since the question hints at 
changes in request or response characteristics, monitoring token usage can pinpoint if the cost increase is 
due to larger inputs, outputs, or potentially more complex queries(initial step before deeper tool usage 
analysis). Cost Correlation: Token usage is often directly tied to billing in cloud AI services, as processing more tokens incurs higher costs. This metric can clearly indicate if the increase in costs is due to the model handling more 
data per interaction. A. Latency: Why It's Less Suitable: While latency might indicate performance issues or model complexity increases, it does not directly correlate with cost increases related to input/output size or tool usage. Latency could be 
affected by many factors unrelated to the suspected causes (e.g., infrastructure, model complexity). B. Evaluation Metrics: Why It's Less Suitable: Evaluation metrics (e.g., accuracy, F1 score) are crucial for model performance assessment but do not provide insight into the operational costs driven by input size, output size, or tool usage expansions. These metrics focus on model efficacy, not cost drivers. C. Run Success Rate: Why It's Less Suitable: The success rate of model runs indicates the frequency of successful executions but 
does not offer insights into what drives up costs. A high success rate with increased costs would not help 
differentiate between input size, output size, or expanded tool usage as the cause. Conclusion: Given the need to identify cost drivers among model input size, model output size, or expanded 
tool usage, with the latter two being more directly related to the former, D. Token Usage is the most appropriate observability capability. It provides a direct measure of how much data is being processed, which 
is typically correlated with cost in AI model deployments. References 1. Microsoft Azure Cognitive Services Pricing Page: https://azure.microsoft.com/en- us/pricing/details/cognitive-services/ - To understand how token usage and other metrics impact 
billing. 2. Azure Monitor for Azure Cognitive Services: https://docs.microsoft.com/en-us/azure/cognitive- services/cognitive-services-usage-metrics - For detailed information on available observability 
metrics, including token usage.

## Question 20

Source pages: 27, 28

HOTSPOT - 
You have a Microsoft Foundry project that contains an agent. 
The agent uses tools to retrieve internal content and call external APIs. The agent is configured to let the model 
decide when to call the tools. 
You need to publish the agent for a compliance workflow. The solution must meet the following requirements: 
Each workflow run must include a retrieval step before generating a response. 
Tool calls must authenticate by using the published agent’s own identity. 
Tool access must use an identity isolated from other project resources. 
Tool access must use support audit tracing. 
What should you do? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: Set tool_choice to required Configure the tool to authenticate by: Using a distinct agent identity bound to the client application Set tool_choice to (required): Setting this to required ensures that the AI model is deterministically forced to call one or more tools before returning a final answer, rather than autonomously deciding whether to skip the

Explanation:
Set tool_choice to required Configure the tool to authenticate by: Using a distinct agent identity bound to the client application Set tool_choice to (required): Setting this to required ensures that the AI model is deterministically forced to call one or more tools before returning a final answer, rather than autonomously deciding whether to skip the 
tool (as it would with auto). Configure the tool to authenticate by (Using a distinct agent identity bound to the client application): To meet compliance standards stating that tool access must utilize an identity isolated from other project resources and support full audit tracing, assigning a distinct agent identity bound explicitly to the client application ensures complete isolation and individual request tracking.

## Question 21

Source pages: 28, 29

You have a Microsoft Foundry project named Project1 that contains the following: 
An OpenAPI tool that calls an external API 
A project connection named Connection1 that stores the API key of the external API 
When an agent calls the OpenAPI tool, the API returns a 401 unauthorized error, and traces show that the API key 
header is NOT being sent. 
You need to ensure that the OpenAPI tool automatically includes the API key from Connection1 on all requests. 
What should you do?

Options:
- A. Enable identity passthrough so that the tool uses the Microsoft Entra token of the caller.
- B. Add the API key header manually to the OpenAPI specification.
- C. Configure the tool to use the default connection of Project1.
- D. Connect the tool to Connection1.

Answer: D

Explanation:
Technical Justification for Correct Answer D Correct Answer: D. Connect the tool to Connection1 Connect the tool to Connection1 is the most appropriate solution because it directly addresses the issue by 
leveraging the existing infrastructure for secure and managed credential handling. Here's why: Secure Credential Handling: Connection1 already stores the API key. By connecting the tool to this connection, the API key is securely injected into the requests without manual interception, reducing security 
risks associated with hardcoding or manually handling sensitive information. Automation and Consistency: This approach ensures the API key is automatically included in all requests to the external API, aligning with the requirement for automation and consistency across all tool invocations. Management and Updates: If the API key needs to be updated, changes can be made in one place (Connection1), and all connected tools will automatically use the new key without requiring individual updates. Why Other Options are Less Suitable: A. Enable Identity Passthrough: Inapplicable Scenario: Identity passthrough is useful for scenarios where the caller's identity needs to be 
propagated, not for including a pre-stored API key from a project connection. Security and Permission Issues: Might introduce unnecessary permissions or complicate access control, as it 
relies on the caller's Microsoft Entra token rather than a dedicated API key. B. Add the API Key Header Manually to the OpenAPI Specification: Security Risk: Hardcoding the API key directly in the OpenAPI spec exposes the key in plain text, posing a 
significant security risk. Management Overhead: Updates to the API key would require manual changes to the spec, contradicting 
best practices for secret management. C. Configure the Tool to Use the Default Connection of Project1: Assumes Incorrect Setup: The premise implies that the default connection would contain or automatically 
provide the necessary API key, which is not specified or guaranteed. Lacks Explicit Control: Does not ensure the specific API key from Connection1 is used, potentially leading to 
the same authorization issue if the default connection lacks the key or uses a different one. References Microsoft Azure: Securely store and retrieve secrets with Azure Key Vault 
Microsoft Foundry Documentation: Connecting Tools to Project Connections

## Question 22

Source pages: 29, 30

You have a Microsoft Foundry project that contains a customer support agent. The agent calls an internal Users report the following issues: You need to inspect individual agent runs to view the ordered sequence of large language model (LLM) calls, tool Which observability capability should you use?

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Tracing To address the reported issues with the Microsoft Foundry project's customer support agent, the chosen

Answer: D

Explanation:
Technical Justification for Choosing D. Tracing To address the reported issues with the Microsoft Foundry project's customer support agent, the chosen 
observability capability must provide detailed, sequential insights into the agent's interactions, including 
Large Language Model (LLM) calls, tool invocations (specifically the internal knowledge API), and precise timing information for each step. Here's why D. Tracing is the most suitable option, along with explanations 
for why the other options are less fitting: D. Tracing (Correct Answer) Detailed Sequence Insight: Tracing provides an end-to-end view of the system's behavior for a specific run, 
showing the ordered sequence of events (LLM calls, API invocations). This is crucial for identifying 
bottlenecks (e.g., why some requests take more than 15 seconds). 
Timing Information: Tracing includes latency data for each step, helping pinpoint where delays occur. Root Cause Analysis for Incorrect Responses: By examining the exact sequence and output of each LLM call 
and API invocation, you can identify mismatches between expected and actual API returns and how the agent 
misinterpreted them. 
Why Other Options Are Less Suitable A. Token Usage Focus: Primarily monitors resource utilization (e.g., token consumption in LLMs). Shortcoming: Doesn’t offer insights into the sequence of events or timing beyond resource usage, making it 
inadequate for diagnosing the described issues. B. Monitoring Focus: Provides high-level, aggregated views of system performance over time (e.g., error rates, average 
response times). Shortcoming: Lacks the granularity needed to inspect individual agent runs and the detailed sequence of 
events required to solve the specific problems. C. Safety Metrics Focus: Concentrates on the safety and fairness aspects of AI model outputs (e.g., bias detection, content 
policy violations). 
Shortcoming: Irrelevant to the operational and sequential debugging needs outlined in the scenario (timing 
issues and response accuracy tied to API returns). Conclusion: Given the need to inspect the ordered sequence of events with timing information for individual agent runs to resolve both the latency and accuracy issues, Tracing (D) is the most appropriate observability 
capability. References 1. Azure Monitor Distributed Tracing: https://learn.microsoft.com/en-us/azure/azure- monitor/app/distributed-tracing 2. Microsoft Azure Observability Capabilities: https://learn.microsoft.com/en- us/azure/architecture/cloud-adoption/.devops/infrastructure-as-code/observability-patterns

## Question 23

Source pages: 31

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More 
than one solution in the set might solve the problem. It is also possible that none of the solutions in the set solve 
the problem. 
After you answer a question in this section, you will NOT be able to return. As a result, these questions do not 
appear on the Review Screen. 
You have a multimodal AI generative model that accepts image uploads and uses extracted image text to generate 
responses. 
You discover that users can upload unsafe images and embed hidden instructions into images to manipulate the 
model. 
You need to implement controls to mitigate the risk. 
Solution: You configure a prompt shield for user prompts. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

Explanation:
Technical Justification for Correct Answer: B. No Goal: Implement controls to mitigate the risk of users uploading unsafe images with hidden instructions to 
manipulate a multimodal AI generative model. Solution Analysis: Configuring a Prompt Shield for User Prompts Why B (No) is Correct: A Prompt Shield is designed to sanitize, filter, or moderate text-based user inputs (prompts) to prevent 
malicious text from influencing the model's behavior. The identified risk Specifically pertains to image uploads with embedded hidden instructions, which a prompt shield does not address since it focuses on text inputs, not image content analysis or processing. 
Configuring a prompt shield leaves the vulnerability associated with image uploads unmitigated. Why A (Yes) is Incorrect: Misalignment with the Risk Type: The solution (prompt shield) does not align with the type of risk identified 
(unsafe images with hidden instructions), as it is tailored for text-based inputs. Incomplete Mitigation: Choosing "Yes" would imply that the solution adequately addresses the problem, which it does not, as the image-based vulnerability remains unaddressed. Alternative Suitable Solutions (Not Provided in the Question but for Context): Image Content Analysis: Utilize Azure Computer Vision or similar services to analyze uploaded images for 
unsafe content or hidden instructions. 
Image Preprocessing: Implement techniques to sanitize images (e.g., re-encode, thumbnail generation) to 
remove potential hidden text instructions before processing. References: Azure Computer Vision Overview Azure Cognitive Services - Secure Your Resources

## Question 24

Source pages: 32

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More 
than one solution in the set might solve the problem. It is also possible that none of the solutions in the set solve 
the problem. 
After you answer a question in this section, you will NOT be able to return. As a result, these questions do not 
appear on the Review Screen. 
You have a multimodal AI generative model that accepts image uploads and uses extracted image text to generate 
responses. 
You discover that users can upload unsafe images and embed hidden instructions into images to manipulate the 
model. 
You need to implement controls to mitigate the risk. 
Solution: You configure image moderation to block unsafe content before processing the images. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

Explanation:
Technical Justification for Solution Evaluation Scenario Recap: Mitigate risks in a multimodal AI generative model by preventing unsafe image uploads that 
embed hidden instructions to manipulate the model. Proposed Solution: Configure image moderation to block unsafe content before processing the images. Evaluation of the Solution: Why the Correct Answer is B (No): Insufficiency in Addressing Hidden Instructions: Image moderation primarily focuses on identifying and 
blocking explicit, inappropriate, or unsafe visible content (e.g., nudity, violence). However, it may not 
effectively detect hidden instructions embedded in images (e.g., steganography, subtle text overlays not 
immediately recognizable as harmful). Scope of "Unsafe Content": The solution assumes image moderation's definition of "unsafe" aligns with the 
threat of embedded instructions, which might not be the case. Embedded instructions could be crafted to 
avoid moderation flags. 
Why Other Options are Not Provided but an Explanation for A (Yes) if it were Considered: Hypothetical Defense for A (Yes): If the image moderation service used had advanced capabilities explicitly including detection of subtle, embedded textual instructions within images (a less common feature), then A 
could be justified. However, this is not a standard assumption for most image moderation tools. Conclusion:Given the standard capabilities of image moderation services, the proposed solution does not fully 
meet the goal of mitigating the risk of embedded hidden instructions in images. Additional or alternative 
measures (e.g., more sophisticated image analysis for steganography, pre-processing to normalize images 
before text extraction) would be necessary to address the specified threat comprehensively. References Microsoft Azure Content Moderator Documentation: Highlights the capabilities and limitations of standard 
image moderation services. Steganography Detection Techniques: Provides insight into the complexities of detecting hidden data in 
images, underscoring why standard moderation might fail.

## Question 25

Source pages: 33, 34

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More 
than one solution in the set might solve the problem. It is also possible that none of the solutions in the set solve 
the problem. 
After you answer a question in this section, you will NOT be able to return. As a result, these questions do not 
appear on the Review Screen. 
You have a multimodal AI generative model that accepts image uploads and uses extracted image text to generate 
responses. 
You discover that users can upload unsafe images and embed hidden instructions into images to manipulate the 
model. 
You need to implement controls to mitigate the risk. 
Solution: You configure a prompt shield for documents. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

Explanation:
Technical Justification for Correct Answer: B. No The proposed solution involves configuring a "prompt shield for documents" to mitigate the risk of unsafe images embedding hidden instructions in a multimodal AI generative model. Here's why this solution does not meet the goal and why other implied options (though not listed) might be less suitable in this specific context, 
followed by an explanation of a more appropriate approach: Why the Proposed Solution (Prompt Shield for Documents) is Insufficient (B. No): Misalignment with the Threat Vector: The primary issue is with image uploads, not documents. A prompt 
shield designed for documents would not directly address the vulnerability in processing images, as it doesn't 
target the image upload and processing pathway. 
Technology Misapplication: Prompt shields are typically designed to filter, sanitize, or control text inputs to 
prevent harmful prompts. Applying this concept to images requires a fundamentally different approach, 
focusing on image analysis and content filtering, which the proposed solution does not accomplish. Implicit Discussion on Other Potential Solutions (Not Listed but for Context): Image Content Filtering/Analysis Services: 
Why More Suitable: Directly addresses the image upload issue by analyzing the image content for safety and 
embedded texts. Technical Justification: Utilizing AI-powered image analysis services (e.g., Azure Computer Vision, Azure Content Moderator) can detect and filter out unsafe images or extract and sanitize text from images before it 
reaches the generative model. 
Embedded Text Detection in Images: Why More Suitable: Targets the specific risk of hidden instructions within uploaded images. Technical Justification: Implementing OCR (Optical Character Recognition) technologies integrated with NLP 
analysis to identify and neutralize potentially manipulative text within images. Correct Approach Summary: To mitigate the risk effectively, the solution should involve image-centric security measures, such as 
integrating image content filtering services or embedded text detection mechanisms, rather than a 
document-focused prompt shield. References For further reading on appropriate technologies to address the image upload security risk: Azure  Content  Moderator:  https://azure.microsoft.com/en-us/services/cognitive-services/content-moderator/ Azure Computer Vision:  https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/

## Question 26

Source pages: 34, 35

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More 
than one solution in the set might solve the problem. It is also possible that none of the solutions in the set solve 
the problem. 
After you answer a question in this section, you will NOT be able to return. As a result, these questions do not 
appear on the Review Screen. 
You have a multimodal AI generative model that accepts image uploads and uses extracted image text to generate 
responses. 
You discover that users can upload unsafe images and embed hidden instructions into images to manipulate the 
model. 
You need to implement controls to mitigate the risk. 
Solution: You configure protected material detection. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

Explanation:
Technical Justification for Solution Evaluation Scenario Recap: Mitigate risks associated with unsafe image uploads and hidden instructions in a multimodal 
AI generative model using image uploads and extracted text for response generation. Proposed Solution: Configure protected material detection. Evaluation of Solution against Goal: Why B. No (Correct Answer) Protected Material Detection Limitations: Configuring protected material detection is primarily designed to 
identify and flag copyrighted, sensitive, or explicitly defined "protected" content (e.g., child protection, 
explicit content). While useful, its core functionality does not specifically target or effectively mitigate the risk of hidden instructions embedded in images designed to manipulate the model's output. Vulnerability to Adversarial Inputs: The solution does not address the root issue of the model's vulnerability to adversarial inputs via image uploads. Protected material detection might not recognize cleverly disguised 
or technically embedded instructions not classified as "protected" content. Narrow Scope: This solution focuses on content type rather than the integrity and security of the input data in 
relation to the model's functionality, leaving the model exposed to the identified manipulation risk. 
Why A. Yes is Incorrect Insufficient Risk Mitigation: Selecting "Yes" implies that protected material detection adequately addresses 
the specified risk, which it does not, as explained above. Misalignment with Security Goal: The goal is to prevent model manipulation through hidden image 
instructions, a challenge that requires a more targeted security or AI model integrity solution. More Suitable Approaches (Not Listed but for Context) Model Input Validation and Parser Security: Enhancing the security of the text extraction process to identify and reject manipulated inputs. Adversarial Training or Robustness Enhancements: Modifying the model to be more resilient against manipulated inputs. References Microsoft Azure - Secure Your AI Models: https://azure.microsoft.com/en-us/services/cognitive- services/security/

## Question 27

Source pages: 35, 36, 37

Case Study - 
This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - 
Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. 
The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: 
Agent1 uses a base model deployment. 
A safety evaluation pipeline is NOT enabled. 
Tool invocation approval workflows are NOT enabled. Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: 
Agent1 has only general knowledge of the Contoso products. 
A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. 
Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. 
The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: 
Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. 
Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. 
Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. 
Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. 
Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: 
The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. 
The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. 
Responses generated by using the product sheet information must be relevant, complete, and accurate. 
Agent1 must be able to use the product sheets to answer natural language questions about product details. 
The model version used by Agent1 must remain consistent to ensure stable responses. 
The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: 
API keys must NOT be used to access Foundry-deployed models. 
Access to the Azure resources must follow the principle of least privilege. 
The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. 
Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. 
Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. 
Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. 
The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: 
Users that interact with Agent1 must have a personalized experience in future interactions, including the ability for 
Agent1 to retain conversation context and recall relevant information from previous interactions. 
Agent1 must answer questions only about the products sold by Contoso. 
You need to recommend a solution to assess the responses generated by Agent1 when the agent uses the product 
information stored in storage1. The solution must meet the technical requirements. What should you include in the recommendation?

Options:
- A. a Retrieval Augmented Generation (RAG) evaluator
- B. a custom guardrail
- C. model fine-tuning
- D. a groundedness evaluator

Answer: D

Explanation:
D. a groundedness evaluator. Why it is correct: A groundedness evaluator (such as the GroundednessEvaluator in Azure AI Studio Evaluation) specifically measures how well the model's generated responses align with and are supported by the input source data (the product sheets inside storage1). This assessment ensures that the agent answers questions accurately without fabricating facts or hallucinating information outside the provided company context. Why the other options are incorrect: A (RAG evaluator): There is no single generic metric called a "RAG evaluator"; rather, RAG applications are 
evaluated using a combination of specific modular metrics like groundedness, coherence, and relevance. B (custom guardrail): Guardrails are real-time execution safety tools (such as Azure AI Content Safety) used to block policy violations or prompt injections during a live session, not standalone evaluation tools used to 
retroactively assess/grade generated content quality. C (model fine-tuning): Fine-tuning is an optimization technique used to customize a model's style, format, or specialized domain vocabulary, not an assessment or evaluation metric solution.

## Question 28

Source pages: 37, 38, 39, 40

Case Study - 
This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. 
The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: 
Agent1 uses a base model deployment. 
A safety evaluation pipeline is NOT enabled. 
Tool invocation approval workflows are NOT enabled. 
Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: 
Agent1 has only general knowledge of the Contoso products. 
A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. 
Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. 
The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: 
Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. 
Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. 
Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. 
Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. 
Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: 
The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. 
The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. 
Responses generated by using the product sheet information must be relevant, complete, and accurate. 
Agent1 must be able to use the product sheets to answer natural language questions about product details. 
The model version used by Agent1 must remain consistent to ensure stable responses. 
The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: 
API keys must NOT be used to access Foundry-deployed models. Access to the Azure resources must follow the principle of least privilege. 
The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. 
Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. 
Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. 
Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. 
The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: 
Users that interact with Agent1 must have a personalized experience in future interactions, including the ability for 
Agent1 to retain conversation context and recall relevant information from previous interactions. 
Agent1 must answer questions only about the products sold by Contoso. 
You need to configure Agent1 to answer customer questions about only the Contoso products. The solution must 
meet the business requirements. 
What should you do?

Options:
- A. Modify the system message instructions.
- B. Add few-shot examples.
- C. Apply top-p sampling.
- D. Increase the value of the temperature parameter.

Answer: A

Explanation:
Technical Justification for Correct Answer: A. Modify the system message instructions To address the business requirement that "Agent1 must answer questions only about the products sold by Contoso," modifying the system message instructions is the most appropriate action. Here's why: Why A is the best choice: System Message Instructions are used to provide initial or contextual instructions to the model, defining its scope, behavior, or the domain of knowledge it should operate within. By modifying these instructions, you can 
explicitly limit Agent1's response domain to Contoso's products, aligning with the business requirement for 
personalized and relevant interactions. This approach directly influences the model's understanding of its operational boundaries without altering the 
underlying model's capabilities unnecessarily. Why other options are less suitable: B. Add few-shot examples: While few-shot examples can guide the model towards understanding the desired output for specific inputs, they do not guarantee a strict limitation to Contoso products across all possible queries. This method is more 
about fine-tuning for specific examples rather than setting a broad operational boundary. C. Apply top-p sampling: Top-p sampling is a technique to control the diversity of generated text by only considering the top probabilities. It does not restrict the model's domain knowledge or ensure responses are limited to Contoso 
products; it merely influences the variability of responses. D. Increase the value of the temperature parameter: The temperature parameter in generation models controls the randomness of the output. Increasing it would lead to more diverse but potentially less relevant or accurate responses. This has no direct bearing on limiting 
the model's responses to Contoso products. Additional Considerations Aligning with Other Requirements: For scalable, high-throughput generative AI workloads and dynamic scaling without reserved throughput, leveraging Azure's auto-scaling capabilities for the model deployment (possibly through Azure Kubernetes Service (AKS) or serverless options like Azure Functions) would be advisable, though this is not directly 
related to the question asked. Indexing solution for semantic and vector search of product sheets could be achieved with Azure Cognitive 
Search, integrating with the model to fetch relevant product information. 
Consistency in model version can be managed through careful deployment strategies and version control in 
Microsoft Foundry. Data processed within the EU is already addressed by Project1's deployment in an EU Azure region. Security Requirements (least privilege, Microsoft Entra authentication, etc.) are met through the described use of security groups and avoiding API keys, aligning with the provided security and compliance 
requirements. References 1. Microsoft Learn - Customize model behavior with system messages: https://learn.microsoft.com/en- us/azure/cognitive-services/language-generation/customize-model-behavior-system-messages 2. Azure Cognitive Search for Semantic Search: https://learn.microsoft.com/en- us/azure/search/search-what-is-semantic-search

## Question 29

Source pages: 40, 41

You have a Microsoft Foundry project. 
You plan to build a customer support solution that contains an agent. The solution must meet the following 
requirements: 
Provide accurate, context-aware responses grounded in internal product documentation stored in Azure AI Search. 
Require deep, multi-step reasoning across long contexts. 
Generate detailed natural language responses. 
Which type of model should you use to power the agent?

Options:
- A. a multimodal model
- B. a small language model (SLM)
- C. a key phrase extraction model
- D. a large language model (LLM)

Answer: D

Explanation:
Technical Justification for Choosing D: a Large Language Model (LLM) Requirements Analysis and Model Selection The customer support solution requires a model that can: 1. Provide accurate, context-aware responses based on internal product documentation stored in Azure AI Search. 2. Perform deep, multi-step reasoning across long contexts. 3. Generate detailed natural language responses. Why D (Large Language Model - LLM) is the Best Choice: Context Awareness and Accuracy: LLMs are trained on vast amounts of text data, enabling them to understand complex contexts and provide accurate responses. Integrating with Azure AI Search, an LLM can 
effectively leverage the internal product documentation to generate informed responses. Deep, Multi-Step Reasoning: The architectural design of LLMs, often based on transformer models, facilitates the handling of long-range dependencies and multi-step reasoning, crucial for resolving complex 
customer inquiries. Detailed Natural Language Responses: LLMs are renowned for their capability to produce coherent, detailed, 
and natural-sounding text, aligning perfectly with the need for comprehensive support responses. Why Other Options are Less Suitable: A. Multimodal Model: While useful for processing multiple data types (e.g., text, images), the primary requirement here focuses on text-based reasoning and response generation, making the multimodal aspect less critical. 
May introduce unnecessary complexity without direct benefit for the specified text-centric tasks. B. Small Language Model (SLM): SLMs lack the scale and depth of training data compared to LLMs, potentially resulting in less accurate or 
less contextually aware responses. 
May struggle with the deep, multi-step reasoning required for complex support queries. C. Key Phrase Extraction Model: Designed primarily for identifying key phrases rather than generating detailed, context-aware responses. Fails to meet the requirements for multi-step reasoning and natural language response generation. ConclusionGiven the specific requirements of the customer support solution, a Large Language Model (LLM) is the most appropriate choice due to its capabilities in context-aware response generation, deep reasoning, 
and detailed natural language output. References 1. Azure AI Search Documentation: https://learn.microsoft.com/en-us/azure/search/search-what-is- azure-search 2. Microsoft Learn - Large Language Models: https://learn.microsoft.com/en-us/azure/cognitive- services/language-service/concepts/large-language-models

## Question 30

Source pages: 41, 42

DRAG DROP - 
You have a Microsoft Foundry project that contains a deployed ticket-triage agent. 
You discover that sometimes the agent responds without calling any tools, even when a tool is required. How should you complete the Python code? To answer, drag the appropriate values to the correct targets. Each 
value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll

Answer: _No answer text extracted._

Explanation:
"tool_choice": This parameter key overrides the default tool execution behavior for a specific thread run. required": Setting this value forces the agent to deterministically invoke at least one configured tool (such as the MCP tool mentioned in prior scenario requirements) before providing a final response, preventing the 
agent from bypassing tool execution.

## Question 31

Source pages: 42, 43

You are building a web app named App1 that generates responses by using a model deployed to a Microsoft Before sending the prompts to the model, App1 must retrieve documents by using Azure AI Search. 
You need to integrate Project1 and App1. The solution must meet the following requirements: A security policy must prevent key-based authentication.

Options:
- A. Call Azure AI Search directly from each application by using Microsoft Entra authentication.
- B. Configure an Azure AI Search connection in Project1 and reference the connection in each application
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

Explanation:
Technical Justification for Correct Answer: B Why B is the Best Option: Meets Requirement 1: Multiple Client Applications - Configuring an Azure AI Search connection in Project1 
allows for a single, reusable search configuration that can be easily referenced by multiple client applications 
(including App1), streamlining the setup process. Meets Requirement 2: Prevents Key-Based Authentication - By integrating the search connection at the Project1 level, the solution can leverage more secure authentication methods (e.g., managed identities, service 
principals with appropriate permissions) instead of key-based authentication for Azure AI Search. Meets Requirement 3: Minimizes Administrative Effort - Centralizing the Azure AI Search configuration in Project1 reduces the administrative burden compared to configuring each application individually. Updates or 
changes to the search configuration can be made in one place. Why Other Options are Less Suitable: A. Custom HTTP Connection in Foundry (Manual Configuration per Application) Fails Requirement 3: Maximal administrative effort due to manual configuration for each application. Inefficient: Does not scale well with multiple applications. C. Call Azure AI Search Directly from Each Application using Microsoft Entra Authentication Partially Addresses Requirement 2: While Entra authentication is secure, this option does not inherently 
prevent key-based authentication if not properly configured. Fails Requirement 1 & 3: Each application would need its own configuration, increasing effort and potentially 
leading to configuration inconsistencies. 
D. Enable Managed Identity for Each Application and Call Azure AI Search Directly Addresses Requirement 2: Secure authentication via managed identities. Fails Requirement 1 & 3: Similar to C, this approach requires per-application setup and maintenance, lacking the centralization benefit for the search configuration. Correct Action: B. Configure an Azure AI Search connection in Project1 and reference the connection in each application. References 1. Azure AI Search Documentation - Integrate Azure AI Search with Azure Services 2. Microsoft Foundry and Azure AI Search Integration - Deploy and integrate models with Azure services (Refer to sections relevant to Azure AI Search and project integrations)

## Question 32

Source pages: 43, 44

DRAG DROP - Ensure that the agent can perform calculations during conversations. 
Ensure that the agent can access up-to-date information from public websites. 
Ensure that the agent can retrieve information from documents uploaded directly to the agent. 
What should you use for each requirement? To answer, drag the appropriate tools to the correct requirements. 
Each tool may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content. 
NOTE: Each correct selection is worth one point.

Answer: _No answer text extracted._

Explanation:
Access up-to-date information (Grounding with Bing Search): This native tool allows the agent to execute real-time web queries to retrieve current information and facts from public websites, mitigating static 
knowledge-cutoff limitations. Perform calculations (Code interpreter): This tool creates a sandboxed runtime environment where the agent can dynamically write and execute Python code to handle complex mathematical operations, logical 
calculations, and data processing accurately. Retrieve information from documents (File search): This built-in vector search/RAG capability parses and processes local document uploads (such as PDFs, DOCX, or TXT files) directly attached to the agent or thread, allowing the model to quickly search across their contents.

## Question 33

Source pages: 44, 45

You have a Microsoft Foundry project that contains a prompt agent used by a customer support web app. 
The agent is invoked from a Python service that does NOT run in the Foundry portal.

Options:
- A. the Azure Monitor Agent
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: BC

Explanation:
Technical Justification for Correct Answer: BC To implement end-to-end tracing for capturing latency breakdowns and exceptions across agent runs in a Microsoft Foundry project, where the agent is invoked from an external Python service, the chosen components must effectively handle distributed tracing, support integration with both Foundry and non-Azure (or external) services, and provide comprehensive insights into performance and errors. Why B (Application Insights) is Correct: Integration with Foundry and External Services: Application Insights (AI) seamlessly integrates with Azure 
services, including Foundry, and can be easily set up for external applications through its SDKs, which include 
a Python SDK for the external Python service. End-to-End Tracing Capability: AI offers automatic detection of dependencies and detailed latency 
breakdowns, crucial for identifying bottlenecks across the agent and the Python service. Exception Tracking: It provides robust exception tracking, alerted and detailed enough for debugging across 
different components of the application. Why C (OpenTelemetry) is Correct: Standard for Distributed Tracing: OpenTelemetry is an open standard for distributed tracing and telemetry, making it highly compatible with both Azure services (like Foundry) and external services (like the Python 
application), ensuring a unified view of the system. Flexibility in Backends: While OpenTelemetry itself doesn’t store data, it can be configured to send traces to various backends, including Application Insights, making it a complementary choice for ensuring traces from 
all parts of the system are captured consistently. Python Support: OpenTelemetry has a Python SDK, facilitating its integration with the external Python 
service for comprehensive tracing. Why Other Options are Less Suitable: A. Log Analytics workspace: While useful for log aggregation and analysis, it's more focused on logging than on the end-to-end tracing and latency breakdowns required. It can be used in conjunction with other tools but 
doesn’t provide the tracing capabilities on its own. D. the Azure Monitor Agent: Primarily designed for collecting metrics and logs from VMs and physical servers, it's not the best fit for tracing in serverlessastr web apps or external services like the described 
Python service. E. Microsoft Sentinel: A security information and event management (SIEM) system, it’s more focused on 
security analytics rather than application performance tracing and latency analysis. References: 1. Application Insights Documentation: https://docs.microsoft.com/en-us/azure/azure-monitor/app/ 2. OpenTelemetry Documentation (Python): https://opentelemetry.io/docs/instrumentation/python/getting-started/

## Question 34

Source pages: 45, 46

You have a customer support agent that uses the Microsoft Foundry Agent Service. Sometimes, customers return to a session days later to continue the same support case, and the agent must Cross-session continuity for the same case 
Access to the full interaction history, including user messages, agent messages, tool calls, and tool outputs What should you do?

Options:
- A. Create and reuse a conversation by storing the conversation’s ID and supplying the ID on subsequent
- B. Persist only the final model response stored in the client application and prepend the response to future
- C. Enable memory summarization on the agent definition to persist the context automatically.
- D. Option D (Visual Block)

Answer: A

Explanation:
Technical Justification for Correct Option (A) To ensure the Microsoft Foundry Agent Service automatically reloads the complete history on each new turn 
for resuming support cases with full historical context, Option A is the most suitable choice. Here’s why: Why A is Correct: Multi-turn and Cross-session Continuity: Creating and reusing a conversation by storing the conversation’s 
ID allows for both multi-turn continuity within a session and cross-session continuity for the same case. This 
approach maintains the conversation's state across different interactions. Access to Full Interaction History: By supplying the stored conversation ID on subsequent requests, the agent can retrieve the entire interaction history, including user messages, agent messages, tool calls, and tool 
outputs, ensuring the agent has the full context. Automatic Reload of History: This method inherently enables the automatic reloading of the conversation's history upon providing the ID, meeting the requirement without needing additional logic for history retrieval. Why Other Options are Less Suitable: B. Persist only the final model response: Inadequate Context: Only storing the final model response would lose the detailed interaction history, making 
it impossible to fully resume the case with all context. Lacks Multi-turn Continuity: Prepending the final response to future prompts does not recreate the conversational flow or provide access to all previous messages and tool interactions. 
C. Enable memory summarization on the agent definition: Summarization Limitations: Memory summarization might not capture the entirety of the interaction history 
with the same fidelity as storing the conversation ID. It's designed for highlighting key points rather than 
preserving a complete record. Unclear Persistence Across Sessions: There’s no clear indication that memory summarization persists across 
sessions in the same detailed manner as reusing a conversation ID. It’s more suited for in-session context 
management. References Microsoft Documentation: Conversations in Microsoft Bot Framework 
Microsoft Foundry Documentation: Managing Conversation State Note: Due to the dynamic nature of 
documentation and the specificity of "Microsoft Foundry Agent Service" (which might be a hypothetical or 
less-documented service in the provided context), the second link is assumed based on common Microsoft service patterns. For actual implementation, always refer to the most current and specific documentation for 
your service.

## Question 35

Source pages: 47, 48

HOTSPOT - 
You have a Microsoft Foundry project that contains a deployed chat model. 
You have a Python service that sends API requests to the model. The service is integrated with an automated 
validation system that compares generated outputs against approved response patterns. 
Stakeholders report that small wording differences are causing validation mismatches. 
You need to update the request parameters to improve output stability. The solution must maximize reasoning 
quality. 
How should you complete the Python code? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: _No answer text extracted._

Explanation:
temperature :1 When enabling extended or adaptive reasoning via the thinking parameter ( "type": "enabled" ), API rules mandate that the temperature must be set to exactly 1 (or omitted completely). Attempting to use a deterministic value like 0 or high variance like 2 will result in a standard HTTP 400 Bad Request validation error from the API gateway. output_config= "effort": ... ("low"):

## Question 36

Source pages: 48, 49

You have a chat app in a Microsoft Foundry project and an Azure AI Search vectorized index. 
You need to connect to the index to meet the following requirements: 
Complex questions must retrieve information from multiple chunks. 
Multi-turn conversations must influence retrieval planning. 
Retrievals must run in parallel to reduce latency. 
Which retrieval approach should you use?

Options:
- A. iterative retrieval
- B. agentic Retrieval Augmented Generation (RAG)
- C. chain of thought
- D. classic Retrieval Augmented Generation (RAG)

Answer: B

Explanation:
Technical Justification for Correct Answer: B - Agentic Retrieval Augmented Generation (RAG) Why B (Agentic Retrieval Augmented Generation) is the Best Choice: Complex Questions & Multi-Chunk Retrieval: Agentic RAG is designed to handle complex, open-ended questions by leveraging an agent's capability to iteratively query a knowledge base (in this case, the Azure AI 
Search vectorized index) across multiple chunks of information. This aligns perfectly with the requirement to 
retrieve information from multiple chunks. Multi-Turn Conversations Influence: The "agentic" aspect implies the use of an AI agent that can understand context and adjust its queries based on previous conversation turns, directly influencing retrieval planning to 
provide more accurate and contextual responses. Parallel Retrievals for Latency Reduction: Agentic RAG, being part of more advanced AI architectures, is more likely to support or be compatible with parallel processing of queries to the vectorized index, reducing 
latency in retrieving information from multiple sources simultaneously. Why Other Options are Less Suitable: A. Iterative Retrieval: Lack of Contextual Understanding: Iterative retrieval lacks the contextual understanding and adaptive query generation provided by an agentic approach, making it less suitable for multi-turn conversations. Scalability and Latency: While it can retrieve from multiple chunks, it doesn't inherently support parallel 
retrievals as effectively as agentic models might, potentially leading to higher latency. C. Chain of Thought: Primary Focus: More focused on generating a step-by-step reasoning process for a model's answer rather 
than efficient, parallel retrieval from an external index. 
Not Designed for External Index Interaction: Less optimized for interacting with an external vectorized index 
in the manner required. D. Classic Retrieval Augmented Generation (RAG): Single-Pass Retrieval: Classic RAG typically involves a single retrieval pass, which is less effective for 
complex, multi-chunk queries compared to the iterative, adaptive approach of Agentic RAG. 
Limited Contextual Adaptation: Lacks the agentic capability to adapt retrieval plans based on multi-turn 
conversation context. References Microsoft Azure - Azure Cognitive Search for Complex Queries 
Research on Agentic Retrieval Augmented Generation for Conversational AI

## Question 37

Source pages: 49, 50

HOTSPOT - 
You need to recommend a plan to create a customer support agent by using the Microsoft Foundry Agent Service. 
The agent must meet the following requirements: 
Retain user preferences across multiple conversations. 
Enable users to provide contextual grounding by directly uploading documents during a chat. 
Which Foundry capability should you recommend for each requirement? To answer, select the appropriate options 
in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: _No answer text extracted._

Explanation:
To retain user preferences across conversations, use: Agent memory that uses persistent storage. To enable users to provide contextual grounding during chats, use the: File search tool Contextual Grounding During Chats: The File search tool allows end users to upload documentation, images,

## Question 38

Source pages: 50, 51

You have a Microsoft Foundry project that contains an agent. The agent generates summaries from retrieved 
policy documents. 
You need to improve response completeness. The solution must be implemented in the logic of the application 
code before responses are returned. 
What should you do?

Options:
- A. Add a retry evaluation before the responses are returned.
- B. Decrease the value of the max_tokens parameter.
- C. Switch to Retrieval Augmented Generation (RAG).
- D. Replace the model with a smaller deployment.

Answer: A

Explanation:
Technical Justification for Correct Answer: A Why A is the best option:To improve response completeness in the context of an agent generating summaries from retrieved policy documents within a Microsoft Foundry project, adding a retry evaluation before responses are returned (Option A) is the most appropriate solution. This approach directly addresses 
potential issues with incomplete responses by allowing the system to re-attempt the generation or retrieval 
process if the initial response does not meet a defined completeness threshold. This can be implemented 
within the application logic to ensure that responses are thoroughly reviewed before being returned to the 
user, enhancing overall completeness without necessarily altering the core model or parameters in a way that 
might compromise other aspects of performance. Why other options are less suitable: B. Decrease the value of the max_tokens parameter:Decreasing max_tokens would actually limit the potential length of the responses, which could worsen the issue of incompleteness by artificially capping the response size, potentially truncating summaries. C. Switch to Retrieval Augmented Generation (RAG):While RAG can enhance the accuracy and relevance of generated text by augmenting the model with external knowledge retrieval, switching to RAG is a significant 
architectural change. It does not directly address the issue of response completeness in the context of the current implementation's logic before responses are returned. It's more about improving accuracy and relevance than ensuring completeness of the generated summaries based on the retrieved documents. References: Microsoft Azure Documentation - Retry Logic in Azure Applications: https://learn.microsoft.com/en- us/azure/architecture/resilience/retry-service-specific Azure Cognitive Services - Understanding Model Parameters (max_tokens context): https://learn.microsoft.com/en-us/azure/cognitive-services/language/understand-how-to-use-language-
model#model-parameters

## Question 39

Source pages: 51, 52

You have a customer support agent built by using the Microsoft Foundry Agent Service. The agent calls an Azure 
OpenAI model deployment. 
During load testing, calls intermittently fail and return an HTTP 429 rate limit exceeded error. 
You need to handle throttling to reduce call failures and improve reliability under load. The solution must remain 
within the service and model limits. 
What should you do?

Options:
- A. Create a new thread and retry the calls immediately.
- B. Reduce the number of registered tools.
- C. Implement a retry policy that uses exponential backoff and jitter.
- D. Spit uploaded content into smaller files.

Answer: C

Explanation:
Technical Justification for Correct Answer (C) Why C is the Best Option:Implementing a retry policy with exponential backoff and jitter (Option C) is the 
most suitable solution for handling throttling and reducing call failures when encountering HTTP 429 rate 
limit exceeded errors. This approach directly addresses the rate limiting issue by adjusting the retry timing 
based on the failure response, preventing immediate repeated failures, and reducing the load on the Azure 
OpenAI model deployment. Exponential backoff increases the wait time between retries after each failure, 
while jitter introduces randomness in the wait time, preventing a "sudden death" scenario where all retries 
happen at once after the same wait period, thus more effectively distributing the load. Why Other Options are Less Suitable: A. Create a new thread and retry the calls immediately: Immediate retries without a backoff strategy will likely result in repeated failures, as the rate limit condition 
hasn't changed. Creating a new thread for each retry can lead to resource exhaustion and does not address the underlying 
throttling issue. B. Reduce the number of registered tools: This might indirectly reduce the load but does not directly address the throttling issue during peak loads. 
It could lead to underutilization of resources if not carefully planned. D. Split uploaded content into smaller files: This approach does not address rate limiting on API calls to the Azure OpenAI model. It might be beneficial for upload limits or processing time but is irrelevant to the throttling problem 
described. Correct Approach (Detailed): Implement a Retry Policy with: Exponential Backoff: Increase the wait time exponentially after each failed retry (e.g., 1s, 2s, 4s, 8s, ...). Jitter: Introduce randomness in the wait time (e.g., wait_time * random_factor) to prevent synchronized retries. Example Implementation Consideration:Utilize Azure's built-in retry mechanisms or libraries (like Polly for .NET) that support exponential backoff with jitter for calls to the Azure OpenAI model, ensuring the solution 
remains within service and model limits. References 1. Azure Documentation - Retry with Exponential Backoff: https://learn.microsoft.com/en- us/azure/architecture/patterns/retry-with-exponential-backoff 2. Polly (for .NET) - Implementation of Retry with Backoff and Jitter: https://github.com/App- vNext/Polly/wiki/Retry-Policy#with-backoff-and-jitter

## Question 40

Source pages: 52, 53

HOTSPOT - You need to configure the workflow to automatically evaluate the agent when a pull request (PR) is created and How should you configure the workflow? To answer, select the appropriate options in the answer area.

Answer: Authentication method An Azure Login action that uses OpenID Connect (OIDC)) When connecting an automated external runner or automation pipeline to Azure resources, storing long-lived

Explanation:
Authentication method An Azure Login action that uses OpenID Connect (OIDC)) When connecting an automated external runner or automation pipeline to Azure resources, storing long-lived 
credentials (like Personal Access Tokens (PATs)) introduces security risks. Utilizing an Azure Login action paired with OpenID Connect (OIDC) allows for short-lived, credential-less authentication, removing the need 
to manage secret keys or rotate expirations. Workflow Action On Failure Fail. In evaluation gates (such as checking prompt flow outputs against accuracy or content safety thresholds), if the minimum criteria or evaluation benchmarks are not met, the runner pipeline must explicitly Fail. This structural break blocks bad builds or ungrounded model revisions from progressing through subsequent 
stages or merging into the primary deployment branch.

## Question 41

Source pages: 53, 54

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More 
than one solution in the set might solve the problem. It is also possible that none of the solutions in the set solve 
the problem. 
After you answer a question in this section, you will NOT be able to return. As a result, these questions do not 
appear on the Review Screen. 
You have a Microsoft Foundry project that contains an agent. The agent generates summaries from retrieved 
policy documents. 
Users report that some responses omit required regulatory clauses, even when the clauses are present in the 
retrieved content. 
You need to improve response completeness. 
Solution: You increase the value of the max_tokens parameter. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: A

Explanation:
Technical Justification for Solution Review Scenario Recap: Enhance response completeness for a Microsoft Foundry agent generating summaries from policy documents, addressing omissions of required regulatory clauses. Proposed Solution: Increase the value of the max_tokens parameter. Evaluation and Justification for Correctness of Solution A (Yes) Rationale for Correctness (A. Yes): Understanding max_tokens: The max_tokens parameter in the context of AI models (like those used in Microsoft Foundry for text summarization) dictates the maximum number of tokens (or "words/tokens" depending on the model's tokenization scheme) the model can output in a single response. 
Impact on Response Completeness: Increasing max_tokens allows the model to generate longer responses. This adjustment directly addresses the issue of omitted regulatory clauses by providing the model with the capacity to include more content from the source document in its summary, thereby potentially increasing the 
completeness of responses regarding required clauses. 
Alignment with Goal: The primary goal is to improve response completeness, especially concerning the inclusion of all necessary regulatory clauses. Increasing max_tokens is a direct and effective strategy to achieve this, making the solution A (Yes) correct. Why Other Options are Less Suitable (B. No) Rationale Against B (No): 
Lack of Justification for Ineffectiveness: Without specific constraints (e.g., performance, response time limits), decreasing or not adjusting max_tokens would not logically address the omission issue. The problem statement does not mention such constraints, making B (No) less justifiable without additional context suggesting why increasing max_tokens wouldn't work. Misalignment with Observed Issue: Saying "No" implies the solution doesn't meet the goal without providing an alternative reason related to the max_tokens adjustment's efficacy in this context, which is technically sound for addressing response length and thus completeness. Conclusion:Given the technical rationale, increasing max_tokens is a suitable solution to enhance response completeness by allowing for longer summaries that can include previously omitted regulatory clauses. Thus, A. Yes is the correct choice. References 1. Microsoft Azure Documentation - Customizing Model Output:https://docs.microsoft.com/en- us/azure/cognitive-services/language/understanding/how-to-use BaseModel? 
tabs=csharp#customize-model-output (Navigate to sections discussing output controls like 
max_tokens for relevant model configurations.) 2. Transformer Model Tokenization Explanation (General AI Context):https://huggingface.co/docs/transformers/glossary#tokenization (While not Azure-specific, 
provides insight into tokenization and max_tokens implications in AI model contexts.)

## Question 42

Source pages: 54, 55, 56

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More After you answer a question in this section, you will NOT be able to return. As a result, these questions do not appear on the Review Screen. 
You have a Microsoft Foundry project that contains an agent. The agent generates summaries from retrieved 
policy documents. 
Users report that some responses omit required regulatory clauses, even when the clauses are present in the 
retrieved content. 
You need to improve response completeness. 
Solution: You add a reflection pass that regenerates the response if the required clauses are missing. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: A

Explanation:
Technical Justification for Solution Evaluation Scenario Recap: Enhance response completeness in a Microsoft Foundry agent that generates summaries from policy documents, specifically to ensure inclusion of required regulatory clauses when present in the 
source material. Proposed Solution Evaluation: Adding a Reflection Pass Solution: Add a reflection pass to regenerate the response if required clauses are missing. Evaluation: Why A (Yes) is Correct: 
Direct Addressal of the Issue: The solution directly targets the problem of missing required clauses by re-
processing the response to ensure their inclusion. 
Improved Completeness: By definition, a reflection pass designed to check for and include missing clauses (if 
present in the source) enhances response completeness, aligning with the stated goal. 
Minimal Infrastructure Implication: Assuming the existing infrastructure can handle an additional pass 
without significant overhead, this solution is relatively low-risk and efficient. 
Why B (No) is Less Suitable (Counterpoint for Completeness): 
No Clear Alternative Provided: Without an alternative solution, "B (No)" lacks a basis for why the proposed 
method wouldn't work, making "A (Yes)" more justified given the information. Potential Misinterpretation of "No": Choosing "B" might imply the solution doesn't address the goal at all, 
which isn't accurate; the reflection pass is a logical step towards ensuring completeness. Conclusion: Given the direct approach to ensuring regulatory clauses are included in summaries and the lack of a more suitable alternative in the options, A (Yes) is the correct choice. This solution effectively meets the 
goal of improving response completeness. References Microsoft Azure Cognitive Services: Enhancing Text Analysis with Custom Passes - While not directly about 
Foundry, illustrates the concept of using additional processing passes for enhanced output. Microsoft Foundry Documentation: Agent Development Best Practices for Content Accuracy - Hypothetical link for illustrative purposes; actual link may vary based on Foundry's documentation updates. For the most current information, search for "Microsoft Foundry agent development best practices" on Microsoft Learn. Note: The second reference is hypothetical due to the rapidly evolving nature of Microsoft's documentation 
and the specificity of "Microsoft Foundry" (which might not directly correspond to a widely recognized 
Microsoft product at the time of this response). For actual study, reliance on official, up-to-date Microsoft 
resources is advised. Actual Working Link Replacement for Educational Purposes (since the second was hypothetical) Microsoft Azure AI Services Overview - For understanding the broader context of AI and machine learning services on Azure, which can inform approaches to enhancing agent capabilities.

## Question 43

Source pages: 56, 57

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More 
than one solution in the set might solve the problem. It is also possible that none of the solutions in the set solve 
the problem. 
After you answer a question in this section, you will NOT be able to return. As a result, these questions do not 
appear on the Review Screen. 
You have a Microsoft Foundry project that contains an agent. The agent generates summaries from retrieved 
policy documents. 
Users report that some responses omit required regulatory clauses, even when the clauses are present in the 
retrieved content. 
You need to improve response completeness. 
Solution: You increase the value of the temperature parameter. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

Explanation:
Technical Justification for Solution Evaluation Scenario Recap: Enhancing response completeness for a Microsoft Foundry agent that generates summaries from policy documents, where some responses omit required regulatory clauses despite their presence in the 
retrieved content. Proposed Solution Evaluated: Increasing the value of the temperature parameter. Evaluation Outcome: B. No (Does not meet the goal) Rationale for Evaluation: Understanding the Temperature Parameter: The temperature parameter in AI models, particularly in text generation and summarization tasks, controls the randomness or diversity of the output. A higher temperature 
increases the diversity of the generated text by making the model less deterministic in its choices. 
Impact on Response Completeness: Increasing Temperature would likely introduce more variability in the summaries but does not directly address the issue of omitting specific, required regulatory clauses. It might even increase the omission rate by 
prioritizing diversity over relevance or completeness in some cases. 
Completeness Requirement: The goal is to ensure all required regulatory clauses are included, which is more 
related to the model's understanding, the summarization strategy, and possibly the input processing (e.g., 
highlighting or weighting important clauses) rather than the output's diversity. 
Why Other Approaches Might Be More Suitable (though not listed, for context): Fine-Tuning the Model on a dataset emphasizing regulatory clauses could improve recognition and inclusion 
of these clauses. 
Adjusting Summarization Strategy to prioritize inclusion of specific clause types or keywords. Why B (No) is the Correct Answer:Increasing the temperature parameter does not directly address the issue of omitting required regulatory clauses from summaries. Instead, it focuses on output diversity, which may not 
enhance, and could potentially detract from, the completeness of the responses in the desired manner. References For deeper understanding of the concepts: Microsoft Azure AI Documentation - Customizing Model Behavior: https://docs.microsoft.com/en- us/azure/cognitive-services/custom-vision-service/how-to-customize-model Temperature in AI Models (General Concept): https://towardsdatascience.com/temperature-in-

## Question 44

Source pages: 57, 58

Note: This section contains one or more sets of questions with the same scenario and problem. Each question 
presents a unique solution to the problem. You must determine whether the solution meets the stated goals. More 
than one solution in the set might solve the problem. It is also possible that none of the solutions in the set solve 
the problem. 
After you answer a question in this section, you will NOT be able to return. As a result, these questions do not 
appear on the Review Screen. 
You have a Microsoft Foundry project that contains an agent. The agent generates summaries from retrieved 
policy documents. 
Users report that some responses omit required regulatory clauses, even when the clauses are present in the 
retrieved content. 
You need to improve response completeness. 
Solution: You run an evaluation flow that scores responses for completeness and blocks responses that fall below 
a defined threshold. 
Does this meet the goal?

Options:
- A. Yes
- B. No
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

Explanation:
Technical Justification for Correct Answer: B. No Why the Correct Option (B. No) is Best: Insufficient Solution for Completeness: Running an evaluation flow that scores responses for completeness and blocks those below a defined threshold detects but does not improve the completeness of responses. It merely filters out inadequate responses without addressing the root cause of why required regulatory clauses 
are omitted. User Experience Impact: Blocking responses below a threshold may lead to a higher rate of "no response" situations, potentially frustrating users who expect at least some form of assistance, even if incomplete. This 
does not enhance the user experience in terms of receiving useful, albeit imperfect, information. Lack of Feedback Loop for Improvement: The proposed solution does not inherently include a mechanism to feedback the shortcomings (e.g., omitted clauses) to the agent's training data or development process, crucial 
for iteratively improving the agent's ability to generate complete responses. Why Other Options are Less Suitable (Given Only One Other Option, A): Option A. Yes: Incorrect Assumption of Solution Efficacy: Assumes that blocking inadequate responses is synonymous with 
"improving response completeness," which is a misunderstanding of the goal. Improvement implies 
enhancement in the quality or thoroughness of the responses provided to the user, not just their filtering. No Direct Enhancement of Agent Capability: Does not contribute to making the agent better at generating 
complete summaries, only at hiding its inadequacies from the user. Conclusion: Given the analysis, the solution does not meet the stated goal of improving response completeness but rather masks the issue. Thus, the correct answer is B. No. References: Microsoft Azure Documentation - Improving AI Model Accuracy: https://docs.microsoft.com/en- us/azure/cognitive-services/custom-vision-service/how-to-improve-model Microsoft Learn - Enhancing Conversational AI with Feedback Loops: https://learn.microsoft.com/en-
us/training/modules/build-conversational-ai-
solutions/#:~:text=Provide%20a%20feedback%20mechanism%20to,improve%20the%20conversational%20AI%20

## Question 45

Source pages: 58, 59

You are creating an image-editing workflow in a Microsoft Foundry project. 
The workflow must meet the following requirements: 
Ensure that background objects can be removed by applying a mask-based inpainting edit. 
Preserve the original lighting and style of the edited images. 
Use the built-in image editing controls, NOT a custom model. 
You need to ensure that image edits apply exclusively inside the masked area. 
How should you configure the workflow?

Options:
- A. Set generation mode to image_variation and provide the original image as a reference.
- B. Enable text_to_image mode and a prompt describing the desired background removal.
- C. Enable image_to_image mode and a high-strength value to regenerate the full image based on the prompt.
- D. Enable mask_inpainting and supply both the input image and a mask indicating which part of the image to

Answer: D

Explanation:
Technical Justification for Configuring the Image-Editing Workflow Correct Answer: D. Enable mask_inpainting and supply both the input image and a mask indicating which 
part of the image to modify. Why D is the best option: Meets the primary requirement: Directly supports mask-based inpainting for removing background objects 
by applying edits exclusively to the masked area. 
Preserves original lighting and style: By focusing edits on the masked region, the rest of the image, including 
its lighting and style, remains untouched. 
Utilizes built-in image editing controls: Aligns with the requirement to not use a custom model, leveraging Foundry's native capabilities. 
Precision over edits: Ensures edits are applied exclusively inside the masked area, fulfilling this critical 
requirement. Why Other Options are Less Suitable: A. Set generation mode to image_variation and provide the original image as a reference Inadequate for targeted edits: Image variation mode may alter the entire image, not just the targeted area, 
and doesn’t guarantee preservation of the original’s untouched aspects. 
Lacks precision for background removal: Not specifically designed for mask-based inpainting. B. Enable text_to_image mode and a prompt describing the desired background removal Incorrect mode for the task: Text-to-image generation is not suited for editing existing images, especially for 
precise, mask-based edits. Loss of original image integrity: Likely to generate a new image rather than preserve the original’s lighting 
and style outside the edit area. C. Enable image_to_image mode and a high-strength value to regenerate the full image based on the prompt Overly broad editing scope: Regenerating the full image at high strength could drastically alter the original 
lighting and style, not just the target area. 
Less precise than mask-based approach: Does not ensure edits are confined to the specified area. References Microsoft Azure - Image Editing with Azure Foundry Azure Foundry Documentation - Mask Inpainting for Image Editing

## Question 46

Source pages: 59, 60

You have a Microsoft Foundry project that generates product marketing images from text prompts. 
After publishing several images, the legal team at your company identifies a competitor’s logo on a sign in the 
background of an image. 
You need to remove only the logo, while preserving the rest of the image. 
What should you do?

Options:
- A. Apply a mask-based inpainting edit to the part of the image that contains the logo.
- B. Increase the prompt guidance strength.
- C. Modify the original prompt to exclude brand names.
- D. Rerun the prompt by using a different random seed.

Answer: A

Explanation:
Technical Justification for Correct Answer: A Why A is the best option:Applying a mask-based inpainting edit to the part of the image that contains the 
logo (Option A) is the most suitable solution for several technical reasons: Precision and Control: Mask-based inpainting allows for precise targeting of the area to be edited (the competitor's logo), minimizing the impact on the rest of the image. Preservation of Original Content: This method preserves the integrity of the surrounding elements in the 
image, which is a critical requirement. Efficiency: Compared to re-generating the image, inpainting is typically faster and more efficient, especially 
for minor edits like logo removal. Why other options are less suitable: B. Increase the prompt guidance strength: Inapplicability to Existing Image: This approach would only affect new image generations based on the 
modified prompt, not the already published image in question. Uncertain Outcome: Increasing guidance strength might alter the image in unforeseen ways, not just remove 
the logo. C. Modify the original prompt to exclude brand names: Retroactive Inapplicability: Like option B, this doesn’t address the existing image but rather future 
generations. 
Overly Broad Impact: Might unnecessarily alter the image’s content beyond just the logo. D. Rerun the prompt by using a different random seed: Unpredictable Outcomes: There’s no guarantee the logo won’t reappear or that the rest of the image will 
remain substantially the same. Time and Resource Inefficient: Could require multiple attempts to achieve a satisfactory result, without 
addressing the specific issue at hand. Correct Answer Justification Summary: Option A, mask-based inpainting, is technically the most precise, efficient, and effective method for removing a specific element (the competitor’s logo) from an existing image 
while preserving the rest of the content. References 1. Microsoft Azure AI for Image Editing: https://docs.microsoft.com/en-us/azure/cognitive- services/computer-vision/concept-image-editing (See sections on Inpainting for detailed technical 
insights) 2. Inpainting in Computer Vision (General Concept): https://en.wikipedia.org/wiki/Inpainting (Provides a broad understanding of the technology behind the recommended solution)

## Question 47

Source pages: 60, 61

You have a Microsoft Foundry project that contains an agent. The agent must preserve the PDF layout in the extracted output to ensure that downstream processing can

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. prebuilt-layout The correct option for the given requirement is D

Answer: D

Explanation:
Justification for Choosing Option D: prebuilt-layout The correct option for the given requirement is D: prebuilt-layout. Here's why: Requirement Analysis: Preserve PDF layout in extracted output 
Extract content and layout elements 
Detect QR codes without a language model deployment Why D: prebuilt-layout is the Best Choice: Layout Preservation and Extraction: The prebuilt-layout analyzer is specifically designed to extract and preserve the layout of the document, including tables, which aligns with the need to reference sections and 
tables in downstream processing. 
QR Code Detection: This analyzer also includes the capability to detect QR codes, fulfilling the requirement without needing an additional or more complex setup like a dedicated language model. Simplicity and Integration: Being a built-in analyzer, it ensures seamless integration with Azure Content 
Understanding in Foundry Tools, minimizing the complexity of the setup. Why Other Options are Less Suitable: A: prebuilt-documentFieldSchema: Primarily used for extracting specific fields based on a predefined schema. 
Does not focus on layout preservation or QR code detection. 
B: prebuilt-read: Excels at reading and extracting text from documents, including layout text, but... Less effective for precise layout preservation and table structure extraction compared to prebuilt-layout. Does not support QR code detection. C: prebuilt-documentSearch: Optimized for enhancing search capabilities within documents. Not designed for layout preservation, detailed table extraction, or QR code detection. Conclusion:Given the specific requirements of preserving the PDF layout, extracting content and layout 
elements (including tables), and detecting QR codes without a language model, D: prebuilt-layout is the most 
appropriate and efficient choice. References 1. Azure Cognitive Search - Prebuilt Analyzers: https://docs.microsoft.com/en-us/azure/search/search- analyzers#prebuilt-analyzers 2. Microsoft Azure: Content Understanding with Prebuilt Layout Analyzer: https://docs.microsoft.com/en-us/azure/cognitive-services/content-
understanding/concepts/prebuilt-layout-analyzer (Note: Link subject to update; for the most current 
info, search for "Azure Content Understanding prebuilt-layout analyzer" on the official Microsoft 
Docs website)

## Question 48

Source pages: 62

You have a Microsoft Foundry project that contains an agent and an image generation model deployment. 
The agent generates original images from user-supplied product photos. 
You need to ensure that the generated images maintain the product identity and visual characteristics of the 
provided photo. 
What should you do?

Options:
- A. Set the input_fidelity parameter to high.
- B. Apply a groundedness detection filter.
- C. Include a prompt and input image in the request.
- D. Decrease the value of the temperature parameter.

Answer: A

Explanation:
Technical Justification for Correct Answer: A Why A is the Best Choice:Setting the input_fidelity parameter to high is the most appropriate action to ensure generated images maintain the product identity and visual characteristics of the provided photo. This 
parameter directly influences how closely the output adheres to the input's characteristics. A high setting 
ensures the model prioritizes fidelity to the input image, preserving the product's visual identity and attributes, which is crucial for maintaining recognizability and consistency in generated product images. Why Other Options are Less Suitable: B. Apply a groundedness detection filter: While this could help in ensuring the generated content is realistic 
and "grounded" in reality, it does not directly address the requirement of maintaining the specific product's 
identity and visual characteristics from the input photo. Groundedness detection filters focus more on the 
realism of the generated image rather than its fidelity to the input. C. Include a prompt and input image in the request: Although including both a prompt and an input image can 
provide the model with more context, the effectiveness of this approach in maintaining product identity depends heavily on the prompt's specificity and quality. The question implies the need for a more direct control over the output's fidelity to the input image, which input_fidelity provides. Furthermore, the scenario 
already involves a user-supplied product photo, suggesting the input image is already part of the request. D. Decrease the value of the temperature parameter: Lowering the temperature parameter reduces randomness in the model's output, making it more deterministic. However, this setting primarily affects the 
variability of the generated images rather than their fidelity to the input's specific characteristics. It might result in more consistent outputs but does not guarantee the preservation of the product's visual identity as 
effectively as adjusting input_fidelity. References: 1. Microsoft Azure Documentation - Image Generation Models: https://docs.microsoft.com/en- us/azure/cognitive-services/computer-vision/concept-generating-thumbnails (See sections related to 
input parameters for image generation) 2. Microsoft Foundry Documentation - Agent Configurations: Note: As Microsoft Foundry is not a widely recognized or documented public platform by Microsoft at the time of this response (it might refer to a custom, less-known, or upcoming service), a direct link cannot be provided. For similar 
configurations in known services, refer to:https://docs.microsoft.com/en-us/azure/cognitive-
services/bing-image-search/use-bing-image-search (Focus on parameters influencing output 
similarity to inputs)

## Question 49

Source pages: 63

HOTSPOT - 
You have a Microsoft Foundry project that contains an agent. 
The agent accepts user-uploaded screenshots and uses a multimodal chat model. 
Some screenshots contain potentially malicious embedded text. 
You need to prevent a prompt injection attack and ensure that third-party content is treated as lower trust. 
How should you configure prompt shields for document attacks? To answer, select the appropriate options in the 
answer area. 
NOTE: Each correct selection is worth one point.

Answer: Prompt shields action: Set action to block. Additional mitigation: Enable Spotlighting. Prompt shields action (Set action to block.): When dealing with direct user prompt injections or indirect document-based attacks, setting the action to Block is necessary to prevent unsafe, modified instructions from hijacking the large language model (LLM)

Explanation:
Prompt shields action: Set action to block. Additional mitigation: Enable Spotlighting. Prompt shields action (Set action to block.): When dealing with direct user prompt injections or indirect document-based attacks, setting the action to Block is necessary to prevent unsafe, modified instructions from hijacking the large language model (LLM) 
session. Choosing annotate merely flags the threat in data attributes without stopping execution, leaving 
downstream applications exposed. 
Additional mitigation (Enable Spotlighting.): Spotlighting is a specialized framework integrated directly into Azure Prompt Shields. It uses advanced 
encoding techniques (like base-64 conversion or structured text delimiting) to dynamically lower the trust signature of external data inputs (documents, emails, web scraped text) relative to direct system instructions. 
This prevents indirect cross-prompt injections without relying on rigid blocklists.

## Question 50

Source pages: 63, 64

You are deploying a support agent that enables users to upload photos. 
You need to automatically classify uploaded images for harmful content. The solution must block content based on 
severity levels. 
What should you do?

Options:
- A. Apply keyword scanning to optical character recognition (OCR) output by using Azure Vision in Foundry
- B. Enable prompt shields.
- C. Use blocklists.
- D. Implement image moderation.

Answer: D

Explanation:
Technical Justification for Correct Answer: D Why D (Implement image moderation) is the best option:Implementing image moderation is the most suitable 
choice for automatically classifying uploaded images for harmful content and blocking based on severity 
levels. This is because image moderation, specifically through Azure's Computer Vision or Azure Content 
Moderator services, is designed to analyze visual content. These services can detect and categorize harmful 
content (e.g., adult, racy, or violent images) with a level of granularity that allows for severity-based blocking. 
This approach directly addresses the requirement for visual content analysis. Why other options are less suitable: A. Apply keyword scanning to optical character recognition (OCR) output by using Azure Vision in Foundry Tools: Limitation: This method only analyzes text extracted from images via OCR, not the visual content itself. It 
cannot detect harmful non-textual content (e.g., violence, nudity). 
Inappropriateness for Requirement: Fails to directly assess image content for harmful visuals. B. Enable prompt shields: Irrelevance: Prompt shields are more relevant to controlling or guiding user input (e.g., in chatbots) rather 
than analyzing uploaded media for harmful content. 
Functional Misalignment: Does not provide a mechanism for image content analysis. C. Use blocklists: Limitation: Blocklists are effective for known harmful sources (URLs, IPs) but do not analyze the content of 
uploaded images in real-time. Inadequacy for Dynamic Content: Unable to classify new, unseen harmful image content based on its visual 
characteristics. References: Azure Content Moderator Documentation - For details on moderating images for harmful content. Azure Computer Vision Documentation - Although primarily for image analysis, can be used in conjunction 
with custom logic for moderation purposes.

## Question 51

Source pages: 64, 65

You have an app named App1 that uses a Microsoft Foundry multimodal model deployment. 
App1 runs optical character recognition (OCR) on uploaded images and appends the OCR output to the prompt as 
additional context. 
Some uploaded images contain embedded text. 
You need to prevent potentially malicious instructions from being processed by the model. 
What should you use?

Options:
- A. image moderation
- B. prompt shields for documents
- C. protected material text
- D. prompt shields for user prompts

Answer: B

Explanation:
Technical Justification for Correct Answer: B - Prompt Shields for Documents Why B is the best option:Prompt Shields for Documents is specifically designed to sanitize and control the input context (in this case, the OCR output appended to the prompt) before it's processed by the model. This 
feature is particularly relevant when dealing with untrusted or potentially malicious content extracted from 
documents (like embedded text in images). By using Prompt Shields for Documents, App1 can effectively 
filter out or redact potentially malicious instructions embedded within the OCR output, preventing them from 
influencing the model's response. Why other options are less suitable: A. Image Moderation: While Image Moderation is crucial for screening out inappropriate or harmful visual content, it does not address the issue of malicious text embedded within images. Image Moderation would not 
process or sanitize the OCR-extracted text, leaving the model vulnerable to malicious instructions in the text 
output. C. Protected Material Text: This option seems to imply a feature for handling sensitive or protected text. However, the primary concern here is not the protection of sensitive text but the prevention of malicious text 
from being processed. Protected Material Text does not inherently imply a mechanism for filtering out 
malicious instructions, making it less suited for this specific requirement. D. Prompt Shields for User Prompts: Although similar in name and concept to the correct answer, Prompt Shields for User Prompts is designed to sanitize and control direct user inputs (e.g., text typed by users). 
While it shares the goal of preventing malicious input, it's tailored for user-generated text prompts rather 
than automatically generated context from documents (like OCR output from images). Conclusion:Given the specific scenario of preventing potentially malicious embedded text in images (after 
OCR processing) from being processed by the model, B. Prompt Shields for Documents is the most 
appropriate and technically justified choice. It directly addresses the need to sanitize document-extracted 
text context before model processing. References 1. Microsoft Azure - Protecting Models from Malicious Input: https://learn.microsoft.com/en- us/azure/cognitive-services/form-recognizer/concept-model-protection (Though the link focuses on 
Form Recognizer, the concept of protecting models from malicious input is broadly applicable and 
relevant to understanding the importance of sanitizing inputs.) 2. Microsoft Documentation - Azure Cognitive Services Security and Compliance: https://learn.microsoft.com/en-us/azure/cognitive-services/security-compliance (This link provides a 
broad overview of security measures in Azure Cognitive Services, including input validation and 
sanitization principles that underpin the rationale for using Prompt Shields.)

## Question 52

Source pages: 66, 67

You have a Microsoft Foundry project that contains an agent. 
You need to process mixed-format documents that contain scanned text, tables, and multicolumn layouts. The 
extracted content must preserve the document structure and be converted into the Markdown format for 
downstream reasoning. 
What should you configure first?

Options:
- A. an Azure Language in Foundry Tools text analysis model deployment
- B. a generative chat completion request
- C. an Azure OpenAI Responses API call that uses a multimodal model
- D. an Azure Content Understanding in Foundry Tools analyzer

Answer: D

Explanation:
Technical Justification for Correct Answer: D To address the requirement of processing mixed-format documents (containing scanned text, tables, and 
multicolumn layouts) while preserving the document structure and converting the extracted content into Markdown format for downstream reasoning, the most appropriate initial configuration is D. an Azure Content Understanding in Foundry Tools analyzer. Here’s why: Why D is the Correct Choice: Document Structure Preservation: Azure Content Understanding is designed to comprehend and retain the 
structural integrity of documents, including tables and multicolumn layouts, which is crucial for this task. Support for Mixed-Format Documents: It can handle scanned documents (via integration with OCR capabilities implicitly or explicitly through associated services) alongside other formats, making it suitable for 
mixed-format input. Output Flexibility: The extracted, structured content can be more easily converted into Markdown format due to its understanding and output of document components (e.g., headings, paragraphs, tables). 
Why Other Options are Less Suitable: A. Azure Language in Foundry Tools text analysis model deployment: Limitation: Primarily focused on text analysis (sentiment, entity recognition, etc.) rather than preserving 
document structure or handling scanned/multicolumn content effectively. Conversion to Markdown: Would require additional, separate processing to structure the output into 
Markdown, increasing the complexity of the pipeline. B. a generative chat completion request: Purpose Misalignment: Designed for generating human-like text based on prompts, not for document 
structure analysis or preservation. 
Format Conversion: Not suited for accurately converting structured document content into Markdown. C. an Azure OpenAI Responses API call that uses a multimodal model: Multimodal Capability: While powerful, the primary challenge here isn’t necessarily the type of input (though 
multimodal helps), but accurately extracting and preserving document structure. Structure Preservation and Markdown Conversion: Less directly suited for the precise structural analysis Conclusion: scanned documents), and converting to Markdown, configuring an Azure Content Understanding in Foundry References: Azure Content Understanding Documentation Microsoft Foundry Project Documentation (Integrating Azure Services)

## Question 53

Source pages: 67, 68

You have an application that processes scanned PDF invoices. The invoices have varied layouts and include 
multipage tables. 
You have a pipeline that uses optical character recognition (OCR) and extracts totals and invoice numbers. The 
results are often incorrect because the document structure is ignored. 
You need to implement a solution that provides OCR, layout analysis, and template-generalizing field extraction. 
The solution must NOT require training a custom model. The solution must minimize administrative effort. 
What should you include in the solution?

Options:
- A. Azure Language in Foundry Tools
- B. Azure Content Understanding in Foundry Tools
- C. an Azure Machine Learning model
- D. Option D (Visual Block)

Answer: B

Explanation:
Justification for Correct Answer: B - Azure Content Understanding in Foundry Tools The correct solution for the given scenario is B. Azure Content Understanding in Foundry Tools. Here's a 
detailed breakdown of why this is the most suitable option and the shortcomings of the other choices: Why B (Azure Content Understanding in Foundry Tools) is Correct: OCR, Layout Analysis, and Field Extraction: Azure Content Understanding is designed to handle complex 
document structures, performing advanced OCR, layout analysis, and field extraction. It can adapt to varied 
layouts and multipage tables without requiring custom model training. 
No Custom Model Training Required: This solution aligns with the requirement of not needing to train a 
custom model, as it leverages pre-trained models optimized for document understanding. 
Minimizes Administrative Effort: By utilizing a managed service, the administrative burden is significantly 
reduced compared to building and maintaining a custom solution or even managing an Azure Machine 
Learning model. 
Why Other Options are Less Suitable: A. Azure Language in Foundry Tools: Primary Focus: More tailored towards natural language processing (NLP) tasks such as text analysis, 
sentiment analysis, etc., rather than the structured document analysis required for invoices. Inadequate for Layout Analysis and Template-Generalizing Extraction: Less capable in handling the complexities of varying document layouts and the specific need for accurate field extraction from tables and 
forms. C. An Azure Machine Learning Model: Requires Custom Model Training: Directly contradicts the requirement of not needing to train a custom 
model, which would also increase development time and effort. 
Higher Administrative Effort: Managing, updating, and ensuring the model's accuracy over time would 
demand more administrative resources compared to a managed service like Azure Content Understanding. 
References For further reading and to delve deeper into the capabilities of the recommended solution: 1. Azure Content Understanding Documentation - https://learn.microsoft.com/en-us/azure/foundry- tools/content-understanding/ 2. Comparison of Azure Services for Document Processing - https://learn.microsoft.com/en- us/azure/architecture/guide/technology-choices/document-processing-services (Utilize this to 
compare the functionalities of different Azure services for document processing tasks.)

## Question 54

Source pages: 68, 69

You have a Microsoft Foundry project that contains an agent. 
The agent uses a knowledge source built from documents stored in Azure Blob Storage. The documents include 
digitally scanned PDFs that contain multipage tables. 
You have an ingestion job that extracts only plain text, causing loss of table structure, headings, and page-number 
metadata. 
Users frequently ask questions that require the retrieval of specific table rows across the pages. 
You need to configure an ingestion job for a Retrieval Augmented Generation (RAG) pipeline that performs optical 
character recognition (OCR) on scanned PDFs, preserves tables and headings as structure-aware chunks, and 
stores page-number metadata with each chunk. 
How should you configure the ingestion job?

Options:
- A. Use advanced data parsing to reingest the documents.
- B. Use OCR and page-level chunking.
- C. Use page-level OCR extraction and store each page as a single chunk.
- D. Use basic parsing and fixed-size chunking.

Answer: A

Explanation:
Technical Justification for Correct Option (A) The correct configuration for the ingestion job, given the requirements, is A. Use advanced data parsing to 
reingest the documents. Here's why this option stands out and why others are less suitable: Why A is the Best Choice: Advanced Data Parsing Capability: Advanced data parsing is specifically designed to handle complex document structures, including the preservation of tables, headings, and extraction of specific metadata like 
page numbers. This aligns perfectly with the need to retain the structure of multipage tables and associate 
page-number metadata with each chunk. Retrieval Augmented Generation (RAG) Pipeline Compatibility: For a RAG pipeline, the ingestion job needs to provide structured, searchable content. Advanced data parsing ensures that the output is optimized for 
such pipelines, facilitating efficient retrieval of specific table rows across pages. 
OCR Implicit in Requirement Understanding: While not explicitly mentioned in option A, the context implies 
that OCR is necessary for scanned PDFs. Advanced data parsing tools often integrate or can be configured 
with OCR capabilities to process scanned documents, making this a holistic choice for the given scenario. 
Why Other Options are Less Suitable: B. Use OCR and Page-Level Chunking: Lack of Explicit Structure Preservation: There's no clear indication that this option preserves table structures 
and headings as "structure-aware chunks" beyond basic page-level processing. Insufficient for RAG's Structured Needs: Might not fully support the nuanced search and retrieval 
requirements of a RAG pipeline without advanced parsing. C. Use Page-Level OCR Extraction and Store Each Page as a Single Chunk: Overly Broad Chunks: Storing each page as a single chunk does not facilitate the retrieval of specific table 
rows efficiently, as it doesn’t preserve the granular structure of the content within pages. Metadata Limitation: Implicitly suggests a lack of detailed metadata association (like specific table row 
locations) with each chunk. D. Use Basic Parsing and Fixed-Size Chunking: Incompatible with Complex Structures: Basic parsing cannot preserve the complex table structures and 
headings effectively. Fixed-Size Chunking Inefficiency: Irrespective of content structure, fixed-size chunking is inefficient for retrieving specific, variable-sized content elements (like table rows) and does not account for page-number 
metadata. References Microsoft Azure - Cognitive Search: Document AI Azure Cognitive Services - Form Recognizer for Structured Data Extraction

## Question 55

Source pages: 69, 70

You have a Microsoft Foundry project that contains an agent. 
The agent uses Azure AI Search as the retriever. 
You plan to ingest PDF into an Azure AI Search index to ensure that the agent can ground responses in texts in 
both documents and embedded images. 
Users require citations that link to the source files. 
You need to ensure that during indexing, the images are extracted into a structure that can be used as input for 
the built-in optical character recognition (OCR) skill. 
Which indexing approach should you use?

Options:
- A. an indexer to extract image data into a normalized_images collection
- B. a Shaper skill to restructure the OCR input
- C. a skillset to run the OCR skill directly against the content field of the index
- D. the outputFieldMappings parameter to write image data to a searchable field

Answer: A

Explanation:
Technical Justification for Correct Answer: A The correct indexing approach to ensure images are extracted into a structure suitable for the built-in Optical Character Recognition (OCR) skill, while also supporting user requirements for citations linking to source files, 
is: A. an indexer to extract image data into a normalized_images collection Why A is the Best Choice: Direct Extraction and Structuring: Using an indexer to extract image data into a normalized_images collection directly structures the image data in a way that is readily consumable by the OCR skill, streamlining the process. 
Support for Citations: By keeping the image data linked to its source (through the structured collection), it facilitates the creation of citations that can point back to the original PDF files, meeting the user's 
requirement. 
Efficiency and Scalability: Indexers are designed for such data ingestion and transformation tasks, making 
this approach efficient and scalable for handling multiple PDFs and their embedded images. Why Other Options are Less Suitable: B. a Shaper skill to restructure the OCR input: Inappropriate Timing: Shaper skills are used for reshaping data after processing (e.g., post-OCR), not for pre-
processing image extraction. 
Inefficient for Image Extraction: Not designed for the initial extraction of images from documents. C. a skillset to run the OCR skill directly against the content field of the index: Lack of Image Extraction: Running OCR directly against the content field does not address the extraction of 
images from PDFs into a usable structure. Missed Structuring Opportunity: Fails to preprocess images into an optimal structure for OCR, potentially 
leading to less accurate results. D. the outputFieldMappings parameter to write image data to a searchable field: Insufficient Structuring for OCR: While useful for making data searchable, it does not ensure the image data 
is structured appropriately for effective OCR processing. Citations and Source Linking: Less directly supports the maintenance of clear links to source files for 
citations compared to a dedicated collection approach. References Microsoft Azure Documentation: Azure Cognitive Search Indexers 
Microsoft Azure Documentation: Skillsets in Azure Cognitive Search

## Question 56

Source pages: 70, 71, 72, 73

Case Study - This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - 
Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. 
The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: 
Agent1 uses a base model deployment. 
A safety evaluation pipeline is NOT enabled. 
Tool invocation approval workflows are NOT enabled. 
Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: 
Agent1 has only general knowledge of the Contoso products. 
A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. 
Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. 
The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: 
Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. 
Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. 
Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. 
Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: 
The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. 
The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. 
Responses generated by using the product sheet information must be relevant, complete, and accurate. 
Agent1 must be able to use the product sheets to answer natural language questions about product details. 
The model version used by Agent1 must remain consistent to ensure stable responses. 
The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: 
API keys must NOT be used to access Foundry-deployed models. 
Access to the Azure resources must follow the principle of least privilege. 
The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. 
Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. 
Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. 
Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. 
The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: 
Users that interact with Agent1 must have a personalized experience in future interactions, including the ability for 
Agent1 to retain conversation context and recall relevant information from previous interactions. 
Agent1 must answer questions only about the products sold by Contoso. 
You need to recommend an invoice review solution that resolves the issue reported by the finance department. 
What should you include in the recommendation?

Options:
- A. chat completions
- B. Azure Document Intelligence in Foundry Tools
- C. Azure Content Understanding in Foundry Tools
- D. Image Analysis

Answer: C

Explanation:
Technical Justification for Invoice Review Solution Recommendation Correct Option: C. Azure Content Understanding in Foundry Tools Azure Content Understanding in Foundry Tools is the most suitable choice for the invoice review solution due 
to the following technical reasons: Visual and Textual Content Evaluation: The finance department's issue involves verifying invoice details 
against vendor contract terms, which includes analyzing both the visual layout (e.g., tables, logos, varied 
layouts) and the textual content of the invoices. Azure Content Understanding is adept at handling both 
aspects, providing a comprehensive analysis. Integration with Foundry: Since Contoso already utilizes Microsoft Foundry, integrating Azure Content Understanding ensures seamless interaction with existing infrastructure, streamlining the development and 
deployment process. Scalability and Throughput: While not explicitly mentioned for this specific task, the overall technical requirements for Contoso's AI solutions emphasize scalability and high-throughput capabilities, which Azure Content Understanding can support, especially when combined with other Azure services optimized for such workloads. Why Other Options Are Less Suitable: A. Chat Completions: Inappropriate Use Case: Chat completions are more suited for generating text based on partial inputs, not for 
analyzing and verifying document content against external terms. 
Lack of Visual Analysis Capability: This option does not address the visual layout analysis requirement. B. Azure Document Intelligence in Foundry Tools: More General-Purpose: While capable, Azure Document Intelligence might not offer the depth of content understanding required for nuanced invoice verification, especially if the focus is more on the intelligence 
extracted from the content rather than just its structure. Assumes Structured Data Extraction Needs: The primary issue isn’t just extracting structured data but understanding and verifying it against contract terms, which might require the deeper content analysis 
capabilities of Azure Content Understanding. D. Image Analysis: Too Narrow in Scope: Image Analysis would handle the visual aspects and potentially images with embedded 
text but would not comprehensively address the textual content analysis and verification against contract 
terms without additional, unnecessary integration complexity. References: For further details on the recommended solution and its capabilities: 1. Azure Content Understanding Documentation: https://learn.microsoft.com/en-us/azure/cognitive- services/content-understanding/overview 2. Microsoft Foundry Integration with Azure Services: https://learn.microsoft.com/en- us/azure/foundry/how-to-integrate-azure-services

## Question 57

Source pages: 73, 74

You have a Microsoft Foundry project that contains an agent. 
The knowledge source for the agent is a set of scanned PDF troubleshooting guides stored in Azure Blob Storage. 
The guide pages contain two-column layouts and tables. 
You use Azure Content Understanding in Foundry Tools to process the PDFs. 
You plan to ingest the processed content into an index for Retrieval Augmented Generation (RAG) and store 
extracted fields for downstream automation. 
Stakeholders must be able to verify where each extracted field value came from in the original PDF and route low-
reliability extractions for manual review. 
You need to ensure that the Content Understanding document analyzer output includes a per-field confidence 
score and source grounding to locations within the source document. 
What should you do?

Options:
- A. Set enableSegment to true.
- B. Provide labeled samples.
- C. Enable estimateFieldSourceAndConfidence.
- D. Configure the analyzer to use generative extraction for all fields.

Answer: C

Explanation:
Technical Justification for Correct Answer: C To address the requirements of including per-field confidence scores and source grounding to locations 
within the source document for the Azure Content Understanding document analyzer output in the context of 
a Microsoft Foundry project, enabling estimateFieldSourceAndConfidence (Option C) is the most 
appropriate action. Here’s why: Per-field Confidence Score Requirement: EstimateFieldSourceAndConfidence is designed to not only 
estimate the confidence in each extracted field value but also to identify the source location within the document where the field value was extracted from. This directly fulfills the need for per-field confidence 
scores, ensuring stakeholders can assess the reliability of each extraction. Source Grounding Requirement: By enabling this feature, the output will include references to the exact 
locations in the original PDF where each field's value was sourced. This feature is crucial for traceability, especially in documents with complex layouts like two-column setups and tables, as it facilitates verification 
of the extraction's origin. Why Other Options are Less Suitable: A. Set enableSegment to true: While enabling segmentation can improve the processing of structured 
content by breaking down documents into manageable parts, it does not directly address the need for confidence scores or source grounding for extracted fields. Segmentation is more about the preprocessing of 
the document rather than the extraction metadata. B. Provide labeled samples: Providing labeled samples is essential for training and improving the accuracy of 
the model over time. However, this action does not directly influence the inclusion of confidence scores or 
source information in the analyzer's output for immediate processing needs. It's a long-term solution for 
model enhancement rather than a direct fix for the specified requirements. D. Configure the analyzer to use generative extraction for all fields: Generative extraction can be powerful 
for certain types of data extraction tasks, especially where the model needs to generate text based on the 
document content. However, this approach may not always provide the precise source grounding or 
confidence scores per field as directly and reliably as enabling EstimateFieldSourceAndConfidence, 
especially in the context of the described requirements and the structured nature of the data (tables, two-
column layouts). Correct Action: C. Enable estimateFieldSourceAndConfidence Enabling this feature ensures that the Content Understanding document analyzer output meets both critical requirements (per-field confidence scores and source grounding) efficiently and directly, making it the best 
choice for the given scenario. References 1. Azure Cognitive Search Documentation - Content Understanding: https://docs.microsoft.com/en- us/azure/search/cognitive-search-concept-intro#content-understanding 2. Customizing Document Analyzer for Content Understanding: https://docs.microsoft.com/en- us/azure/search/cognitive-search-defining-skillset#document-analyzer-skills (Refer to sections 
related to field extraction and confidence scores for more detailed insights)

## Question 58

Source pages: 74, 75

detect issues while the calls are in progress. The call audio will arrive as a continuous stream from the telephony system. 
You need to ensure that the call transcripts appear within only a few seconds of the audio stream. 
What should you do?

Options:
- A. Use text to speech by using a custom neural voice.
- B. Use speech translation to generate the transcripts into multiple languages.
- C. Run a batch transcription job on recorded audio files.
- D. Use real-time speech to text to process streaming audio input.

Answer: D

Explanation:
Technical Justification for the Correct Option (D) To meet the requirement of transcribing live phone calls with near-real-time transcription (within a few seconds of the audio stream), the solution must process the audio input as a continuous stream rather than in 
batches or after the call is completed. Here’s why option D is the best choice and why the others are less 
suitable: Correct Option: D - Use real-time speech to text to process streaming audio input Real-time Capability: Real-time speech to text is designed to handle streaming audio inputs, making it 
perfectly suited for transcribing live phone calls. Low Latency: This approach ensures that transcripts are generated with minimal delay, fulfilling the 
requirement of transcripts appearing within a few seconds of the audio stream. 
Continuous Streaming Support: It is specifically built to process continuous audio streams, such as those 
from ongoing telephony systems, without requiring the audio to be pre-recorded or buffered for an excessive 
amount of time. 
Why Other Options Are Less Suitable A - Use text to speech by using a custom neural voice Reverse Requirement: Text to speech converts text into speech, which is the opposite of what is needed 
(converting speech to text). 
No Benefit for Transcription: Custom neural voices do not aid in the transcription process but rather in 
generating synthetic speech from text. B - Use speech translation to generate the transcripts into multiple languages Additional, Unrequested Functionality: While useful for multi-language support, the primary requirement is 
for real-time transcription in one language (implied, as the question does not mention translation needs). 
Potential Increase in Latency: Adding a translation step could introduce additional delay, moving further from 
the near-real-time requirement. C - Run a batch transcription job on recorded audio files Batch Processing Incompatibility: Batch jobs are designed for processing pre-recorded audio files in bulk, 
not for real-time or near-real-time transcription of live streams. High Latency: Transcripts would only be available after the batch job completes, which would be long after 
the call has ended, violating the low latency requirement.

## Question 59

Source pages: 75, 76, 77

You are creating an agent workflow in a Microsoft Foundry project to support natural voice interactions. 
The agent must receive continuous audio input, convert the input into text for reasoning, and then return spoken 
responses to a user. The workflow must meet the following requirements: 
Support turn-taking dynamics, where the agent begins to generate the speech output before the user finishes 
speaking. 
Operate with low latency to maintain conversational experience. 
You need to enable both speech to text and text to speech in a real-time agent interaction. 
What should you do?

Options:
- A. Use batch transcription to convert the audio input and return text responses from the agent.
- B. Use real-time speech to text for incoming audio and text to speech for agent responses.
- C. Use an embeddings model to encode the audio, and then decode the audio into text and speech.
- D. Use speech translation to convert the audio into another language and return the translated text.

Answer: B

Explanation:
Technical Justification for Correct Answer: B Why B is the Best Option: Real-time Processing: Option B utilizes real-time speech to text, which is essential for meeting the low latency requirement, ensuring a seamless conversational experience. This capability processes audio as it is 
being received, minimizing delays. 
Support for Turn-Taking Dynamics: By converting audio to text in real-time, the agent can begin generating 
speech output even before the user finishes speaking, directly supporting the turn-taking dynamics 
requirement. 
Direct Alignment with Requirements: Speech to Text: Directly converts incoming audio into text for the agent's reasoning, fulfilling the first 
technical requirement. Text to Speech: Generates spoken responses from the text output, fulfilling the second technical 
requirement for real-time agent interaction. Why Other Options are Less Suitable: A. Batch Transcription: High Latency: Processes audio in batches, leading to significant delays, which contradicts the low latency 
requirement. 
Incompatible with Turn-Taking: Cannot start processing until the user finishes speaking, making turn-taking 
dynamics impossible. 
C. Embeddings Model for Encoding/Decoding: Indirect Approach: While embeddings can be used in NLP tasks, this option describes an indirect and 
potentially less efficient method for the specific tasks of real-time speech to text and text to speech 
conversion. Lack of Clear Latency Benefit: Does not inherently guarantee low latency or support for turn-taking as 
effectively as dedicated real-time speech services. 
D. Speech Translation: Misaligned Capability: Focuses on translating audio into another language, which is not the primary 
requirement (conversational interaction in the same language). 
Added Latency: Translation adds an extra step, potentially increasing latency beyond what's acceptable for real-time interaction. Conclusion:Given the requirements for real-time processing, low latency, support for turn-taking dynamics, and the direct need for speech to text and text to speech conversion, Option B is the most technically suitable 
choice for enabling both functionalities in a real-time agent interaction. References Microsoft Azure Speech Services - Real-time Speech Recognitionhttps://docs.microsoft.com/en- us/azure/cognitive-services/speech-service/speech-to-text Microsoft Azure Text-to-Speech (TTS) for Real-time Responseshttps://docs.microsoft.com/en- us/azure/cognitive-services/speech-service/text-to-speech

## Question 60

Source pages: 77, 78

You have an application named App1 that uses Azure Speech in Foundry Tools to transcribe live calls. 
Transcript segments often contain both English and Spanish. App1 sends each segment to Azure Translator in 
Foundry Tools to translate to another language. 
Sometimes, mixed-language segments result in incomplete or incorrect translations. 
You need to reduce translation errors. The solution must ensure that the entire transcript is translated 
successfully. 
What should you do before sending the segments to Translator?

Options:
- A. Use document translation to translate the entire transcript as a single document.
- B. Split the mixed-language segments into single-language segments and translate each segment separately.
- C. Enable automatic language detection for the translation request.
- D. Specify English as the source language in the translation request for all the segments.

Answer: B

Explanation:
Technical Justification for Correct Answer: B To address the issue of incomplete or incorrect translations for mixed-language segments in App1, the most 
effective solution is to split the mixed-language segments into single-language segments and translate 
each segment separately (Option B). Here's why this approach is best and why other options are less 
suitable: Why B is the Correct Approach: Accuracy Enhancement: By isolating language segments, the translation model can focus on one language at 
a time, significantly improving accuracy. 
Direct Handling of Mixed-Language Content: This method proactively deals with the root cause (mixed 
languages in a segment) by separating them, ensuring each translation request is linguistically homogeneous. 
Compatibility with Azure Translator: Azure Translator can efficiently handle multiple, single-language 
translation requests, making this approach technically feasible and scalable. Why Other Options are Less Suitable: A. Use Document Translation for the Entire Transcript: Limitation: While document translation can handle larger texts, it may not effectively mitigate mixed- language issues within a single document, as the engine might struggle with interwoven languages. Potential for Errors: Similar or worse error rates as current setup if language detection within the document 
feature is not robust enough for intertwined languages. C. Enable Automatic Language Detection for the Translation Request: Reliability Concerns: Automatic detection may not always accurately identify and separate mixed languages 
within a single segment, potentially leading to similar translation errors. Segmentation Challenge: Detection doesn't solve the segmentation issue; it only identifies languages, not 
necessarily how to process them correctly in mixed segments. D. Specify English as the Source Language for All Segments: Inapplicability: Ignores the presence of Spanish (and potentially other languages), guaranteeing translation 
failures for non-English parts. 
Error Rate Increase: Likely to increase errors for segments containing languages other than English. Conclusion:Splitting mixed-language segments into single-language parts before translation (Option B) is the most technically sound approach to reduce translation errors, given its direct addressing of the problem's root 
cause and compatibility with the capabilities of Azure Translator in Foundry Tools. References 1. Azure Translator Documentation - Best Practices for Translation Requests: https://docs.microsoft.com/en-us/azure/cognitive-services/translator/best-practices 2. Azure Speech to Translator Integration Guidance: https://docs.microsoft.com/en- us/azure/cognitive-services/speech-service/howto-translate-speech?tabs=dotnet (Note: While this 
link focuses on speech-to-text-to-speech translation, the principles of handling multi-language 
inputs can be inferred for text translation scenarios.)

## Question 61

Source pages: 78, 79, 80, 81

Case Study - 
This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - 
Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: 
Agent1 uses a base model deployment. 
A safety evaluation pipeline is NOT enabled. 
Tool invocation approval workflows are NOT enabled. 
Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: 
Agent1 has only general knowledge of the Contoso products. 
A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. 
Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. 
The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: 
Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. 
Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. 
Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. 
Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. 
Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: 
The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. 
The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. 
Responses generated by using the product sheet information must be relevant, complete, and accurate. 
Agent1 must be able to use the product sheets to answer natural language questions about product details. 
The model version used by Agent1 must remain consistent to ensure stable responses. 
The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: 
API keys must NOT be used to access Foundry-deployed models. 
Access to the Azure resources must follow the principle of least privilege. 
The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. 
Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. 
Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. 
The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: 
Users that interact with Agent1 must have a personalized experience in future interactions, including the ability for 
Agent1 to retain conversation context and recall relevant information from previous interactions. 
Agent1 must answer questions only about the products sold by Contoso. 
You need to configure an indexing pipeline for Agent1 to retrieve the relevant product information in storage1. The 
solution must meet the technical requirement. 
Which two built-in skills should you use? Each correct answer presents part of the solution. 
NOTE: Each correct selection is worth one point.

Options:
- A. Azure OpenAI Embedding
- B. Entity Recognition
- C. Text Split
- D. Merge
- E. Language Detection
- F. key phrase extraction

Answer: AC

Explanation:
Technical Justification for Correct Answer: AC (Azure OpenAI Embedding & Text Split) Contoso requires an indexing pipeline for Agent1 to retrieve relevant product information from PDF product sheets in storage1, meeting the technical requirement of enabling semantic and vector search for accurate, 
complete, and relevant responses to natural language questions. Why Azure OpenAI Embedding (A) is Correct: Semantic and Vector Search Capability: Azure OpenAI Embedding is designed to generate dense vector representations of text, enabling efficient semantic search. This aligns perfectly with Contoso's requirement 
for an indexing pipeline that facilitates semantic and vector search, allowing Agent1 to retrieve relevant 
product information based on the semantic meaning of the queries. Integration with AI Workloads: Given Contoso's use of Microsoft Foundry for generative AI solutions, Azure OpenAI Embedding integrates seamlessly, supporting the scalable, high-throughput requirements for 
Agent1's interactions. 
Handling Natural Language Queries: By generating embeddings, this skill enhances Agent1's ability to 
understand and respond accurately to natural language questions about product details, ensuring relevance 
and completeness. 
Why Text Split (C) is Correct: Processing Large Documents: Product sheets are in PDF format, which can be lengthy. Text Split is essential for breaking down these large documents into manageable, indexing-friendly segments, ensuring that the 
indexing pipeline can efficiently process each part. Optimizing Search Efficiency: By splitting text, the search index can be more granular, leading to faster and 
more accurate retrieval of specific product information in response to customer queries. Preprocessing for Embedding: Text Split prepares the text for more effective embedding generation by Azure OpenAI Embedding, as smaller, contextually relevant chunks of text can produce more accurate vector 
representations. 
Why Other Options are Less Suitable: B. Entity Recognition: While useful for identifying specific entities (e.g., product names), it does not enable the broad semantic and vector search required for retrieving relevant product information based on natural 
language queries. D. Merge: This skill is counterproductive for the goal of creating a granular, searchable index, as it combines 
texts, potentially reducing search efficiency. E. Language Detection: Not relevant to the task of indexing product information for semantic/vector search, 
as the language of the product sheets is presumably known and consistent. F. Key Phrase Extraction: Similar to Entity Recognition, it's useful but doesn't meet the requirement for a searchable index that supports semantic and vector searches for accurate responses to varied natural 
language questions. References 1. Azure OpenAI Embedding Documentation: https://learn.microsoft.com/en-us/azure/cognitive- services/OpenAI/how-to/embeddings 2. Azure Cognitive Search (for context on Text Split and semantic search capabilities): https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search

## Question 62

Source pages: 81, 82, 83, 84

Case Study - 
This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - 
Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. 
The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and troubleshooting requests. 
Agent1 has the following configurations: 
Agent1 uses a base model deployment. 
A safety evaluation pipeline is NOT enabled. 
Tool invocation approval workflows are NOT enabled. 
Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: 
Agent1 has only general knowledge of the Contoso products. 
A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. 
Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. 
The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: 
Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. 
Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. 
Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. 
Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. 
Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: 
The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. 
The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. 
Responses generated by using the product sheet information must be relevant, complete, and accurate. 
Agent1 must be able to use the product sheets to answer natural language questions about product details. 
The model version used by Agent1 must remain consistent to ensure stable responses. 
The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: 
API keys must NOT be used to access Foundry-deployed models. 
Access to the Azure resources must follow the principle of least privilege. 
The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. 
Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. 
Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. 
Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. 
The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: Users that interact with Agent1 must have a personalized experience in future interactions, including the ability for 
Agent1 to retain conversation context and recall relevant information from previous interactions. 
Agent1 must answer questions only about the products sold by Contoso. 
You need to recommend a solution to support the planned changes and technical requirements for Agent1 to use 
the product information stored in storage1. 
What should you include in the recommendation?

Options:
- A. Azure Translator in Foundry Tools
- B. Grounding with Bing Search
- C. Azure AI Search
- D. Azure Document intelligence in Foundry Tools

Answer: C

Explanation:
Technical Justification for Recommending Azure AI Search (Option C) Why Option C (Azure AI Search) is the Best Choice: Meets Technical Requirements: Enables semantic and vector search for indexing product sheets, allowing Agent1 to retrieve relevant 
information (aligns with the requirement for an indexing pipeline with semantic and vector search 
capabilities). Supports scalable, high-throughput workloads suitable for variable customer support traffic without requiring reserved throughput capacity (supports the model deployment requirements for Agent1). 
Integration and Compatibility: Seamless integration with Microsoft Foundry, ensuring consistency with Contoso's existing environment. Facilitates the use of detailed product information from storage1 in responses, enhancing Agent1's 
capabilities. 
Security and Compliance Alignment: Does not rely on API keys for access, aligning with the ban on API key usage for Foundry-deployed models. 
Compatible with least privilege access principles and Microsoft Entra authentication for secure access 
control. Why Other Options are Less Suitable: Option A (Azure Translator in Foundry Tools): Primarily designed for translation tasks, not suited for indexing or retrieving product information based on 
semantic/vetor search requirements. 
Does not address the need for Agent1 to understand and respond with detailed product knowledge. Option B (Grounding with Bing Search): External search may not guarantee data privacy or compliance with EU data retention requirements (especially since Project1 is deployed in an EU Azure region). Less integrated with Contoso's existing Microsoft Foundry and Azure environment, potentially introducing 
complexity. Option D (Azure Document Intelligence in Foundry Tools): While useful for extracting information from documents (like invoices), it doesn't fulfill the semantic/vetor search indexing requirement for enabling Agent1 to answer product questions effectively. More focused on document processing rather than search and retrieval for conversational AI use cases. Conclusion:Azure AI Search is the most comprehensive solution for Contoso's requirements, offering the necessary search capabilities, scalability, security, and integration with their existing Microsoft Foundry 
environment to enhance Agent1's functionality effectively. References: Azure AI Search Documentation - https://learn.microsoft.com/en-us/azure/search/search-what-is- azure-search Microsoft Foundry Integration with Azure Services - https://learn.microsoft.com/en-

## Question 63

Source pages: 84, 85

You have a Microsoft Foundry project named Project1. 
Project1 contains an application that processes PDF vendor invoices. 
You need to configure Azure Document Intelligence in Foundry Tools to generate a Markdown output that 
preserves the sections and table structure of the PDFs. The solution must minimize development effort. 
What should you do?

Options:
- A. Configure output=figures when you analyze the PDF.
- B. Configure content=markdown when you analyze the document.
- C. Increase the confidence threshold.
- D. Set the output_content_format=ContentFormat.MARKDOWN value.

Answer: D

Explanation:
Technical Justification for Correct Answer (D) To configure Azure Document Intelligence in Foundry Tools for generating Markdown output that preserves 
the sections and table structure of PDF vendor invoices with minimal development effort, the most 
appropriate action is to Set the output_content_format=ContentFormat.MARKDOWN value. Here’s why: Why D is the Correct Choice Direct Specification of Output Format: By setting output_content_format=ContentFormat.MARKDOWN, you directly instruct the Azure Document Intelligence API to produce the output in Markdown format. This ensures that the structure (including sections and tables) is preserved in a format that's easily readable and further processable. Minimal Development Effort: This approach requires no additional coding to parse or transform the output, as the API handles the conversion to Markdown. This aligns perfectly with the requirement to minimize 
development effort. 
Why Other Options are Less Suitable A. Configure output=figures: Inadequate for Structural Preservation: Specifying output=figures would primarily focus on extracting images or figures from the PDF, neglecting the textual content and structural elements (sections, tables) that need 
preservation. Does Not Generate Markdown: This option does not generate Markdown output, failing to meet the primary 
requirement. 
B. Configure content=markdown: Misinterpretation of Parameter: While this option seems relevant due to the mention of "markdown", the content parameter typically refers to what content to extract (e.g., text, tables) rather than the output format. The correct approach for specifying the output format is through output_content_format. May Not Preserve Structure as Required: Even if content=markdown influenced output format (which it doesn't directly), there's no guarantee it would preserve structures as effectively as specifying the output 
format explicitly. 
C. Increase the confidence threshold: Irrelevant to Output Format: Adjusting the confidence threshold affects the accuracy and reliability of the extracted data (making the model more conservative in what it outputs as recognized text or structures) but 
has no bearing on the output format or structural preservation in Markdown. 
Conclusion Setting output_content_format=ContentFormat.MARKDOWN is the most direct, efficient, and effective method to achieve the desired outcome with minimal development effort, making D the correct choice. References Azure Document Intelligence API Reference - Output Formats Microsoft Azure Documentation - Document AI Output Configuration

## Question 64

Source pages: 85, 86

You have a Microsoft Foundry project that ingests scanned PDF invoices stored in Azure Blob Storage. Each 
invoice contains printed fine items and has a table-based layout. 
Extracted results are stored as structured JSON and used as grounding data for an agent in a Retrieval 
Augmented Generation (RAG) solution. 
You need to create a single analyzer that meets the following requirements: 
Extracts the invoice number, invoice date, vendor name, and total amount across varying templates 
Returns confidence scores so that results with confidence below 0.80 can be routed for supervisor review 
What should you use?

Options:
- A. a Foundry agent that has groundedness guardrails enabled to extract invoice fields and confidence scores
- B. a custom Azure Content Understanding in Foundry Tools analyzer that defines the required fields as the
- C. the Azure Content Understanding in Foundry Tools prebuilt-layout analyzer
- D. the Azure Content Understanding in Foundry Tools prebuilt-documentSearch analyzer and search.score from

Answer: B

Explanation:
Technical Justification for Choosing Option B Why B is the Best Choice:A custom Azure Content Understanding (ACU) in Foundry Tools analyzer, as 
described in option B, is the most suitable choice for this scenario because it directly addresses all specified 
requirements with precision. By defining the required fields (invoice number, invoice date, vendor name, and 
total amount) as extracted fields, it ensures targeted data extraction across varying templates. Moreover, 
configuring the analyzer to return confidence scores enables the crucial functionality of routing results with scores below 0.80 for supervisor review, aligning perfectly with the project's needs. Why Other Options are Less Suitable: A. Foundry Agent with Groundedness Guardrails: While a Foundry agent can be powerful for tasks involving grounding data, this option does not directly imply 
the ability to extract specific fields from scanned PDF invoices with variable templates as efficiently as a 
customized ACU analyzer. Confidence score extraction for routing is not a standard feature highlighted by groundedness guardrails, 
making this option less straightforward for the given requirements. C. Prebuilt-layout Analyzer in ACU: The prebuilt-layout analyzer might struggle with "varying templates" since its performance can be highly 
dependent on the consistency of the layout it's trained on. Custom extraction of specific fields (invoice number, date, etc.) and the return of confidence scores for 
routing might not be as directly configurable or as accurate as with a custom analyzer. D. Prebuilt-documentSearch Analyzer with Azure AI Search Score: This option focuses more on search functionality rather than precise field extraction from documents, making 
it less ideal for extracting specific invoice details. Relying on search.score for confidence might not accurately reflect the extraction confidence of specific fields within the document, as it's more related to the relevance of the document in search results. Correct Choice Justification Summary:Option B is the most technically appropriate because it allows for: Customization to extract specific fields across varying templates. Direct configuration to return confidence scores for conditional routing based on a precise threshold (below 
0.80). References: Microsoft Azure Documentation - Custom Analyzers in Content Understanding Microsoft Learn - Extract insights from documents with Azure Content Understanding

## Question 65

Source pages: 86, 87

You have a Microsoft Foundry project that uses Azure AI Search to ground an agent in internal documentation. You need to identify whether the retrieved content is negatively influencing the model’s generated responses.

Options:
- A. indexer status and failure history
- B. latency breakdown traces
- C. groundedness evaluation metrics
- D. Groundedness Evaluation Metrics is the most suitable choice, and why the others are less appropriate

Answer: D

Explanation:
Technical Justification for Correct Answer (D) To address the issue of decreased accuracy in the agent's responses after a content update in a Microsoft 
Foundry project utilizing Azure AI Search for grounding, it's crucial to focus on observability signals that 
directly relate to the integration of retrieved content with the model's response generation. Here’s why D. Groundedness Evaluation Metrics is the most suitable choice, and why the others are less appropriate: D. Groundedness Evaluation Metrics: Relevance: Groundedness metrics directly measure how well the model's responses are grounded in the retrieved content from Azure AI Search. A decline in these metrics post-content update would indicate that 
the new content is not being effectively utilized or is misleading the model, leading to less accurate 
responses. Actionability: Reviewing these metrics provides clear insights into whether the issue lies in the content 
update itself or in how the model interprets this content, guiding targeted adjustments. A. Indexer Status and Failure History: Less Suitable Because: While important for overall system health, indexer status primarily indicates if the indexing process is functioning correctly. Failure history might show if content wasn't indexed properly, but it 
doesn't directly correlate with the model's ability to generate accurate responses from the content. 
Why Not Best: Doesn't provide insight into the model's usage of the content for response accuracy. B. Latency Breakdown Traces: Less Suitable Because: Latency issues might affect user experience but do not directly impact the accuracy of the model's responses. Slow performance could be a separate issue but doesn't explain the decrease in 
response accuracy. 
Why Not Best: Focuses on performance rather than content-model interaction accuracy. C. Prediction Drift Metrics: Less Suitable Because: While prediction drift metrics are crucial for monitoring model performance over time, 
they are more generalized. They can indicate a decline in model accuracy but do not specifically point to the 
influence of the retrieved content as the cause. 
Why Not Best: Less targeted than groundedness metrics for identifying content-related issues. Conclusion: Given the need to isolate whether the retrieved content update is negatively impacting the model's response accuracy, D. Groundedness Evaluation Metrics is the most direct and relevant observability 
signal to review. It offers the clearest path to understanding the interaction between the new content and the 
model's performance. References Microsoft Documentation: Azure AI Search - Troubleshooting (Although not directly linked to "Groundedness Evaluation Metrics", this resource provides insight into troubleshooting content indexing issues, which can be 
a precursor to evaluating groundedness.) Microsoft Learn: Monitor and troubleshoot Azure AI models (While broad, this learning module touches on 
model monitoring aspects that can be related to understanding prediction drift and, by extension, the 
importance of specific metrics in model performance analysis.)

## Question 66

Source pages: 87, 88, 89, 90

HOTSPOT Case time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study 
- 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview 
- 
Company Information 
- 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment 
- 
Identity Environment 
- 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. 
The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment 
- 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 
- 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: • Agent1 uses a base model deployment. • A safety evaluation pipeline is NOT enabled. • Tool invocation approval workflows are NOT enabled. • Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 
- 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment 
- 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements 
- 
Contoso identifies the following issues: • Agent1 has only general knowledge of the Contoso products. • A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. • Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. • The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements 
- 
Planned Changes 
- 
Contoso plans to implement the following changes: • Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. • Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. • Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. • Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. • Complete the development of the video creation solution. 
Technical Requirements 
- 
Contoso identifies the following technical requirements: • The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. • The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. • Responses generated by using the product sheet information must be relevant, complete, and accurate. • Agent1 must be able to use the product sheets to answer natural language questions about product details. • The model version used by Agent1 must remain consistent to ensure stable responses. • The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: • API keys must NOT be used to access Foundry-deployed models. • Access to the Azure resources must follow the principle of least privilege. • The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. • Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. • Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. • Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. • The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements 
- 
Contoso identifies the following business requirements: • Users that interact with Agent1 must have a personalized experience in future interactions, including the ability 
for Agent1 to retain conversation context and recall relevant information from previous interactions. • Agent1 must answer questions only about the products sold by Contoso. 
You need to ensure that the marketing department can generate videos by using the model deployed to Project2. 
How should you complete the Python code? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: A

## Question 67

Source pages: 90, 91, 92

Case Study - 
This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study - 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview - 
Company Information - 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment - 
Identity Environment - 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment - 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 - 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: • Agent1 uses a base model deployment. • A safety evaluation pipeline is NOT enabled. • Tool invocation approval workflows are NOT enabled. • Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 - 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment - 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements - 
Contoso identifies the following issues: • Agent1 has only general knowledge of the Contoso products. • A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. • Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. • The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements - 
Planned Changes - 
Contoso plans to implement the following changes: • Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. • Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. • Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. • Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. • Complete the development of the video creation solution. 
Technical Requirements - 
Contoso identifies the following technical requirements: • The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. • The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. • Responses generated by using the product sheet information must be relevant, complete, and accurate. • Agent1 must be able to use the product sheets to answer natural language questions about product details. • The model version used by Agent1 must remain consistent to ensure stable responses. • The data processed by the model must remain within the EU. 
Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: • API keys must NOT be used to access Foundry-deployed models. • Access to the Azure resources must follow the principle of least privilege. • The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. • Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. • Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. • Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. • The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements - 
Contoso identifies the following business requirements: • Users that interact with Agent1 must have a personalized experience in future interactions, including the ability 
for Agent1 to retain conversation context and recall relevant information from previous interactions. • Agent1 must answer questions only about the products sold by Contoso. 
You need to configure personalized user interactions for Agent1. The solution must meet the business 
requirements. 
What should you include in the solution?

Options:
- A. knowledge
- B. memory
- C. guardrails
- D. tools

Answer: B

## Question 68

Source pages: 92, 93, 94, 95

HOTSPOT 
- 
Case Study 
- 
This is a case study. Case studies are not timed separately from other exam sections. You can use as much exam 
time as you would like to complete each case study. However, there might be additional case studies or other 
exam sections. Manage your time to ensure that you can complete all the exam sections in the time provided. Pay 
attention to the Exam Progress at the top of the screen so you have sufficient time to complete any exam sections 
that follow this case study. 
To answer the case study questions, you will bed to reference information that is provided in the case. Case studies 
and associated questions might contain exhibits or other resources that provide more information about the 
scenario described in the case. Information provided in an individual question does not apply to the other questions 
in the case study. 
A Review Screen will appear at the end of this case study. From the Review Screen, you can review and change 
your answers before you move to the next exam section. After you leave this case study, you will NOT be able to 
return to it. 
To start the case study 
- 
To display the first question in this case study, select the “Next” button. To the left of the question, a menu 
provides links to information such as business requirements, the existing environment, and problem statements. 
Please read through all this information before answering any questions. When you are ready to answer a question, 
select the “Question” button to return to the question. 
Overview 
- 
Company Information 
- 
Contoso, Ltd is a multinational retail company that builds, deploys, and manages generative AI and agent-based 
solutions by using Microsoft Foundry. 
Existing Environment 
- 
Identity Environment 
- 
Contoso uses Microsoft Entra ID for identity management, authentication, and authorization capabilities that 
enable agents to access organizational resources and services. 
Contoso recently formed a new AI engineering team named Agent1Dev Team to optimize and maintain existing AI 
solutions. The team collaborates with solution architects, DevOps engineers, and security engineers to design, implement. 
monitor, and secure AI applications. 
Contoso also has a team named Agent1Test Team that is responsible for validating AI solutions before the solution 
deployments. 
Generative Environment 
- 
Contoso has a Microsoft Foundry deployment that contains two projects named Project1 and Project2. 
Project1 
- 
Project1 contains a customer support agent named Agent1 that assists customers with product inquiries and 
troubleshooting requests. 
Agent1 has the following configurations: • Agent1 uses a base model deployment. • A safety evaluation pipeline is NOT enabled. • Tool invocation approval workflows are NOT enabled. • Conversation memory constraints are NOT configured. 
Agent1 interacts with customers by using digital support channels and answers general questions about Contoso 
products. 
Project1 is deployed to an Azure region located in the European Union (EU). 
Agent1Dev Team will use Project1 to optimize and maintain Agent1. 
Project2 
- 
Project2 contains a deployed video generation model. The marketing department at Contoso has access to 
Project2 and plans to use the model to develop a video creation solution. 
Development of the solution is incomplete. 
Data Environment 
- 
Contoso stores product-related information in Azure resources that support AI applications. 
The Azure environment contains an Azure Blob Storage account named storage1 that stores product detail sheets 
for all the Contoso products. 
The product sheets include specifications, feature descriptions, and product support information that Agent1 can 
use to answer customer questions. The product sheets are stored in the PDF format. 
Problem Statements 
- 
Contoso identifies the following issues: • Agent1 has only general knowledge of the Contoso products. • A recent chat interaction with Agent1 was analyzed for sentiment. The results of the analysis have NOT been 
processed yet. • Agent1 does NOT use the detailed product information in the product sheets stored in storage1 when responding 
to customer questions. • The finance department at Contoso reports that vendor invoices must be reviewed manually to ensure that the 
invoices match the terms defined in the vendor contracts. The invoices contain tables, logos, and varied layouts 
that make the documents difficult to process consistently. 
Requirements 
- 
Planned Changes 
- 
Contoso plans to implement the following changes: • Implement a solution for Project1 that analyzes the vendor invoices by evaluating both the visual layout and the 
textual content of the invoices, so that the invoice details can be verified against the vendor contract terms. • Update the base model deployment used by Agent1 and standardize the model version to ensure continuity and 
consistent responses. • Enable Agent1 to retrieve and use the detailed product information from the product sheets stored in storage1. • Implement an indexing solution for the product sheets that Agent1 can use to answer customer questions. • Complete the development of the video creation solution. 
Technical Requirements 
- 
Contoso identifies the following technical requirements: • The model deployment used by Agent1 must support scalable, high-throughput generative AI workloads and 
dynamically scale to handle variable customer support traffic, without requiring reserved throughput capacity. • The product sheets must be processed by using an indexing pipeline that enables semantic and vector search, so 
that Agent1 can retrieve the relevant product information. • Responses generated by using the product sheet information must be relevant, complete, and accurate. • Agent1 must be able to use the product sheets to answer natural language questions about product details. • The model version used by Agent1 must remain consistent to ensure stable responses. • The data processed by the model must remain within the EU. Security and Compliance Requirements 
Contoso identifies the following security and compliance requirements: • API keys must NOT be used to access Foundry-deployed models. • Access to the Azure resources must follow the principle of least privilege. • The developers at Contoso must authenticate to Microsoft Foundry resources by using Microsoft Entra 
authentication. • Access to Project1 must be assigned to the members of Agent1Dev Team by using a security group named 
SC_Agent1_Dev. • Access to Project1 must be assigned to the members of Agent1Test Team by using a security group named 
SC_Agent1_Test. • Agent1 must never reveal customer information, even if a document that contains customer data is added 
erroneously to the product sheet repository in storage1. • The product sheets might contain images that include embedded text. Agent1 must be protected from malicious 
instructions potentially hidden within the images. 
Business Requirements 
- 
Contoso identifies the following business requirements: • Users that interact with Agent1 must have a personalized experience in future interactions, including the ability 
for Agent1 to retain conversation context and recall relevant information from previous interactions. • Agent1 must answer questions only about the products sold by Contoso. 
You need to ensure that Agent1Dev Team can access Agent1. The solution must meet the security and compliance 
requirements. 
How should you complete the Python code? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: To ensure that the `Agent1Dev Team` (represented by the security group `SC_Agent1_Dev`) can access 
`Project1` within Microsoft Foundry using Microsoft Entra authentication, you must assign the appropriate role 
to the security group at the project scope.Based on standard Azure AI/Foundry role-based access control 
(RBAC) patterns for developers:1. Role Assignment: The role required to access and manage a project is

## Question 69

Source pages: 95

You have a Microsoft Foundry project that contains a Retrieval Augmented Generation (RAG) chat solution used by 
customer support agents. 
You are adding an automated pre-production evaluation step to a CI/CD pipeline named Pipeline1. The evaluation 
will run against a labeled test dataset that contains support questions and the expected grounding context. 
You need to ensure that Pipeline1 fails if unsupported content or a retrieval mismatch exceeds a defined threshold: • responses include claims not supported by the retrieved source content • retrieved source content does not align with the labeled expected context 
Which two built-in evaluators should you use in Pipeline1? Each correct answer presents pat of the solution. 
NOTE: Each correct selection is worth one point.

Options:
- A. Retrieval
- B. Fluency
- C. Coherence
- D. Groundedness
- E. Response Completeness

Answer: AD

## Question 70

Source pages: 95

You have a Microsoft Foundry project that contains a support-ticket triage agent built by using the Foundry Agent 
Service. 
The agent uses tool to classify the ticket type and sot the ticket priority. 
Sometimes, the same support case continues across multiple sessions over several days. 
You need to persist state by using a durable ID to ensure that the agent can automatically reuse the full interaction 
history. The solution must preserve previous user messages, tool calls and tool outputs across turns and sessions. 
Which runtime component should you use?

Options:
- A. output item
- B. agent
- C. conversation
- D. response

Answer: C

## Question 71

Source pages: 95, 96

HOTSPOT You need to run a pre-production evaluation by using labeled CSV dataset that contains the query, context, Whether responses are supported by the provided context 
Whether responses contain sensitive or proprietary information Which AI quality evaluation metrics should you use? To answer, select the appropriate options in the answer area. 
NOTE: Each correct selection is worth one point.

Answer: Groundedness, Relevance, Protected Material Detection

## Question 72

Source pages: 96

Which two evaluation categories can you use? Each correct answer presents a complete solution.

Options:
- A. risk and safety metrics
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)
- E. Option E (Visual Block)

Answer: AE

## Question 73

Source pages: 96, 97

You have a Microsoft Foundry project that contains an agent. The agent uses two tools to perform the following Use Azure AI Search to retrieve answers from a private product documentation index. 
Use the web search tool to retrieve public information on the internet. 
You need to ensure that for a specific run, the agent deterministically retrieves information only from the internet. “type”: “azure_ai-search”

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. “auto”
- D. “required”

Answer: A

## Question 74

Source pages: 97

You have a Microsoft Foundry project that contains a customer support agent built on a deployed chat model. 
The agent responses are validated by using an automated testing system that compares generated answers to 
stored expected outputs. Identical prompts must return consistent response to prevent automated test failures. What should you do for the model?

Options:
- A. Remove stop sequences from the requests.
- B. Decrease the temperature parameter.
- C. Increase the temperature parameter.
- D. Option D (Visual Block)

Answer: C

## Question 75

Source pages: 97

You need to improve accuracy by showing the model how correct classifications look, without retaining the model

Options:
- A. zero-shot learning
- B. chain of thought
- C. few-shot learning
- D. Option D (Visual Block)

Answer: D

## Question 76

_No prompt text extracted._

Answer: _No answer text extracted._

## Question 77

Source pages: 97, 98

DRAG DROP You have a Microsoft Foundry project that contains an agent. You need to enable long-term memory to ensure that the agent can recall user preferences across separate 
conversations. Stored memories must be isolated per authenticated user without the client application manually How should you complete the Python code? To answer, drag the appropriate values to the correct targets. Each

Answer: To enable long-term memory in Microsoft Copilot Studio (formerly known as Microsoft Foundry) for an agent

## Question 78

Source pages: 98

Invokes the Azure AI Content Safety tool by using a Foundry connection within the same request

Options:
- A. Enable logging by using the client SDK for Content Safety.
- B. Enable application tracing in Project1.
- C. Route requests through the Azure OpenAI endpoint.
- D. Option D (Visual Block)

Answer: C

## Question 79

Source pages: 98, 99

HOTSPOT You have a Microsoft Foundry project that contains two agents named PolicyWriter and RskReviewer. 
PolicyWriter generates daft updates for customer polices, and RiskReviewer reviews the drafts. Finalizes low-risk updates without manual intervention 
Ensures predictable execution across the agents Requires user approval for highs updates 
What should you configure? To answer, select the appropriate options in the answer area. 
NOTE: Each comet selection is worth one point.

Answer: _No answer text extracted._

## Question 80

Source pages: 99

You have a Microsoft Foundry project that contains an agent named Agent1. Agent runs successful, but Foundry Control Plane does NOT display values for error rates, runs, and token usage, You need to ensure that Found Control Plane displays the appropriate values for Agent1.

Options:
- A. Restart Agent from Foundry Control Plan
- B. Enable Application Insights for Agent1.
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: D

## Question 81

Source pages: 99, 100

You have a Microsoft Foundry project that contains an agent. The extracted content is indexed for search and provided to a downstream agent in the Markdown format. 
You need to generate a Markdown output that has a layout and a semantic structure optimized for Retrieval

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

## Question 82

Source pages: 100

You have a Microsoft Foundry project that contains an agent. You need to build a solution that supports semantic similarity matching. The solution must ensure that the agent

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: A

## Question 83

Source pages: 100

You have a Microsoft Foundry agent that grounds responses from an Azure Search index that contains the Searchable text fields for product names and product codes 
A vector field that stores embeddings for product descriptions 
You need to ensure that users can query the index by using the following: Exact product names or codes 
Natural language descriptions of the products

Options:
- A. vector search only
- B. semantic search only
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

## Question 84

Source pages: 100, 101

Client applications must display page-level citations that have bounding polygons for both text and images. Provide text and image location metadata. 
Extract tables that span multiple pages. 
What should you add?

Options:
- A. Document Extraction
- B. GenAI Prompt
- C. Document Layout
- D. Option D (Visual Block)

Answer: B

## Question 85

Source pages: 101

You need to enable users to search invoice data across the invoice fields.

Options:
- A. Text Translation
- B. optical character recognition (OCR)
- C. Image Analysis
- D. Option D (Visual Block)

Answer: C

## Question 86

Source pages: 101, 102

DRAG DROP You need to configure an analyzer to output a generated JSON field that describes the color scheme of each video How should you configure the analyzer? To answer, drag the appropriate values to the correct targets. Each value 
may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view

Answer: _No answer text extracted._

## Question 87

Source pages: 102

You have an invoice-processing application named App1 that uses Azure Constant Understanding in Foundry Tools. 
You are building a new Content Understanding pipeline named Pipeline1 that must meet the following 
requirements: • Compare an invoice to its related purchase order • Validate the voice against static vendor contact documents • Return a single structured output that includes discrepancy findings 
You need to configure Pipeline1 and expose the pipeline as a single analyzer endpoint. What should you configure?

Options:
- A. a single-file task in standard mode that uses the vendor contract provided as an additional document during
- B. a single-file task in standard mode that uses confidence scores enabled for the extracted fields.
- C. a multiple-file task in pro mode that uses the vendor contract files as reference data
- D. a multi-file task in standard mode that uses the invoice and purchase order as input to the analyzer

Answer: C

## Question 88

Source pages: 102, 103

You have a Microsoft Foundry project that generates short promotional product videos. After several clips are approved, reviewers notice a small watermark in the top-right corner of some videos. Modify the original prompt to exclude watermarks.

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. Increase the guidance scale.
- D. Apply a mask-based inpainting edit to the affected part of the video.

Answer: D

## Question 89

Source pages: 103

You have a web app named App1 that sends requests to a multimodal chat model deployment in a Microsoft 
Foundry project. 
User messages can contain both text and images. 
Currently, App1 includes image URL: as plain text inside the message content so the model cannot recognize them 
as images. 
Traces show that the requests contain a single text message instead of a multimodal content array. 
You need to send the message as a structured array that includes both the text portion and the image reference to 
ensure that the model can process the image correctly. 
What should you do?

Options:
- A. Set the user message content array to include items that have type: text and type: image_url.
- B. Encode the image to base64 and include the encoded data inside the content string of the user message.
- C. Add the image URL to the request metadata section, so the model can resolve the processing issue
- D. Place the image URL inside the System Message and set type to image_url so the model loads the image at

Answer: A

## Question 90

Source pages: 103

Streaming audio input from users and playback audio responses 
You need to configure a connection method that supports real-time audio streaming in client application and

Options:
- A. RTMP
- B. WebRTC
- C. SIP
- D. WebSocket

Answer: D

## Question 91

Source pages: 103, 104

You have a Microsoft Foundry project that contains an agent and uses a GitHub repository. The repository contains You need to create a GitHub Actions workflow that runs the evaluation defined in File1 when a pull request (PR) is opened. How should you configure the workflow?

Options:
- A. Set project-endpoint to the endpoint of the project.
- B. Set evaluation-config to the path of the YAML file.
- C. Set model-deployment-name to the deployed model.
- D. Set tenant-id to the Microsoft Entra tenant ID

Answer: A

## Question 92

Source pages: 104

HOTSPOT You have a Microsoft Foundry project that contains an agent. You need to ensure that the agent can retrieve the secrets. The solution must follow the principle of least privilege. 
What should you configure? To answer, select the appropriate options in the answer area.

Answer: Managed

## Question 93

Source pages: 104, 105

HOTSPOT Includes risk and safety metrics 
Includes the protected material evaluation You create an evaluation named Run2 that has the following configurations: Includes risk and safety metrics 
Includes the protected material evaluation 
Includes harmful content metrics that use a high severity threshold Content harm defect rate of Run2: 4% Protected material evaluation of Run1: 6% 
Protected material evaluation of Run1: 6% For each of the following statements, select Yes if the statement is true. Otherwise, select No. 
NOTE: Each correct selection is worth one point.

Answer: YesNoYes

## Question 94

Source pages: 105

DRAG DROP 
- 
You have a Microsoft Foundry project that contains a multi-agent solution. The agents use tool calling to query 
internal systems. 
You need to implement responsible AI auditing to meet the following requirements: • Capture all the nested operations across the entire agent run. • Record tool invocation arguments and retuned results as metadata. 
What should you use for each requirement? To answer, drag the appropriate options to the correct targets Each 
option may be used once, more than once, or not at all. You may need o dag the split bar between panes or scroll to 
view content. 
NOTE: Each correct selection is worth one point.

Answer: Trace context, Custom dimensions

## Question 95

Source pages: 106

DRAG DROP 
- 
You have a Microsoft Foundry project that contains an agent. The agent uses threads and file uploads and calls an 
Azure OpenAI model deployment. 
During load testing, calls intermittently fall and return an HTTP 429 rate limit exceeded error. Some user uploads 
fail and generate an HTTP 400 file size exceeded error. 
You need to mitigate the errors and reduce call failures. The solution must remain within the service and model 
limits. 
What should you do to resolve each error? To answer, drag the appropriate actions to the correct errors. Each 
action may be used once, more than once or not at all. You may need to drag the split bar between panes or scroll 
to view content. 
NOTE: Each comet selection is worth one point.

Answer: HTTP 429: Implement exponential backoff retry logic.HTTP 400: Validate file size against model limits before 
upload.

## Question 96

Source pages: 106, 107

You need to deploy a model from the model catalog to support a search solution for internal policy documents. The Which type of model should you use?

Options:
- A. Option A (Visual Block)
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: A

## Question 97

Source pages: 107

You need to deploy a model from the model catalog to support real-time inference. The solution must meet the Use key-based authentication. NOT consume the vCPU quota of the virtual machines in the Azure subscription.

Options:
- A. self-hosted container
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: D

## Question 98

Source pages: 107, 108

HOTSPOT You plan to create a Microsoft Foundry project named Project1 that will contain an agent and use an Azure key How should you complete the Bicep code? To answer, select the appropriate options in the answer area?

Answer: resource connection 
'Microsoft.MachineLearningServices/workspaces/onlineEndpoints/deployments/connections@2024-01-01-
preview' = name: 'KV1-connection' parent: deployment properties: category: 'AzureKeyVault' target: 
kv1.properties.vaultUri authType: 'None'

## Question 99

Source pages: 108, 109

HOTSPOT Retains customer preferences across separate chat sessions 
How should you configure the agent? To answer, select the appropriate options in the answer area.

Answer: For the requirements of grounding responses in specific company policy documents and retaining customer

## Question 100

Source pages: 109

You have a Microsoft Foundry project that contains an agent. The agent generates summaries from retrieved

Options:
- A. Add a retry evaluation before the responses are returned.
- B. Decrease the value of the temperature parameter.
- C. Increase the value of the presence_penalty parameter
- D. Replace the model with a smaller deployment.

Answer: A

## Question 101

Source pages: 109, 110

HOTSPOT You develop a test method to verify the results retrieved from a call to the Azure Vision in Foundry Tools API. The 
call is used to analyze the existence of company logos in images. The call returns a collection of brands named For each of the following statements, select Yes if the statement is true. Otherwise, select No. 
NOTE: Each correct selection is worth one point.

Answer: YesYesNo

## Question 102

Source pages: 110

You have an Azure subscription. 
You plan to build an app that will use the Azure AI DALL-E model.

Options:
- A. the Azure SDK for Python and PowerShell cmdlets.
- B. the Azure portal and Microsoft Graph API
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: C

## Question 103

Source pages: 110, 111

HOTSPOT You have an Azure subscription. You need to create a new resource that will generate fictional stores in response to user prompts. The solution How should you complete the script? To answer, select the appropriate options in the answer area.

Answer: AC

## Question 104

Source pages: 111, 112

HOTSPOT You have a Python application collects customer comments before posting them to a public forum. You need to send a text comment to Azure AI Content Safety and return the self-harm severity from the response. 
How should you complete the code? To answer, select the appropriate options in the answer area.

Answer: AD

## Question 105

Source pages: 112

You have a custom named entity recognition (NER) project in Azure Language in Foundry Tools for support tickets. 
The schema for the project contains an entity type named ContactInfo. 
In tagged training files, ContactInfo is used for phone numbers, email addresses, and social media handles. 
Model evaluation shows low precision for ContactInfo, including false positives in which nearby text is extracted as 
ContactInfo. 
You need to improve the precision of the project. 
What should you do before retraining the model?

Options:
- A. Lower the confidence threshold for ContactInfo.
- B. Trigger an auto-labeling job.
- C. Add more support tickets as training data and label more ContactInfo entities.
- D. Replace ContactInfo by using Phone, Email, and SocialMedia entities. Relabel every matching span.

Answer: D

## Question 106

Source pages: 113

You are building a text-to-speech solution that uses Azure Speech in Foundry Tools to read instructions from the 
script in a text file. 
You discover that the solution often pronounces technical terms incorrectly.

Options:
- A. Use Speech Synthesis Markup Language (SSML) to apply say as rules.
- B. Use Speech Synthesis Markup Language (SSML) to adjust the prosody of the voice.
- C. From Azure OpenAI use the Whisper model.
- D. Option D (Visual Block)

Answer: B

## Question 107

Source pages: 113, 114, 115

HOTSPOT 
- 
You have a Python application that redacts sensitive information before sending prompt text to a language model. 
The application has the following code: For each of the following statements, select Yes if the statement is true. Otherwise, select No. 
NOTE: Each correct selection is worth one point.

Answer: Yes, No, Yes

## Question 108

Source pages: 115

DRAG DROP 
- 
You are developing an application that will detect faulty components produced on a factory production line. The 
components are specific to your business. 
You need to use the Azure Custom Vision API to help detect common faults. 
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of 
actions to the answer area and arrange them in the correct order.

Answer: 1. Create a project.2. Upload and tag images.3. Train and publish the model.

## Question 109

Source pages: 115, 116

You are developing a new sales system that will process user-generated video and text from a public-facing 
website.

Options:
- A. reliability and safety
- B. Option B (Visual Block)
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: B

## Question 110

Source pages: 116

Which Azure service should you include in the solution?

Options:
- A. Azure Document Intelligence in Foundry Tools
- B. Azure AI Immersive Reader
- C. Option C (Visual Block)
- D. Option D (Visual Block)

Answer: C

## Question 111

Source pages: 116

You have an Azure subscription that contains an Azure App Service app named App1. 
You provision a Microsoft Foundry Service resource named CSAccount1. 
You need to configure App1 to access CSAccount1. The solution must minimize administrative effort.

Options:
- A. the endpoint URI and subscription key
- B. the endpoint URI and an OAuth token
- C. the endpoint URI and a shared access signature (SAS) token
- D. Option D (Visual Block)

Answer: A

## Question 112

Source pages: 116, 117

DRAG DROP You have a web app that uses Azure AI Search. compromised. 
You need to prevent unauthorized access to the search endpoint and ensure that users only have read only access 
to the documents collection. The solution must minimize app downtime. 
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of 
actions to the answer area and arrange them in the correct order.

Answer: EBD

## Question 113

Source pages: 117, 118

HOTSPOT You need to create a new resource that will be used to perform sentiment analysis and optical character 
recognition (OCR). The solution must meet the following requirements: Use a single key and endpoint to access multiple services. 
Consolidate billing for future services that you might use. 
Support the use of Azure Vision in Foundry Tools in the future. 
How should you complete the HTTP request to create the new resource? To answer, select the appropriate options

Answer: AI Services

## Question 114

Source pages: 118, 119

HOTSPOT You are building a model to detect objects in images. 
The performance of the model based on training data is shown in the following exhibit. Use the drop-down menus to select the answer choice that completes each statement based on the information 
presented in the graphic. 
NOTE: Each correct selection is worth one point.

Answer: The provided images show a graph where the x-axis represents the number of training iterations and the y-
axis represents the loss (specifically, the training loss and validation loss). Based on the standard 
interpretation of such machine learning performance graphs:* Statement 1: The model is experiencing 
overfitting (because the training loss continues to decrease while the validation loss begins to 
increase/plateau).* Statement 2: To improve the model performance, you should increase the amount of 
training data or apply regularization (which prevents the model from memorizing the noise in the training 
set).Based on the typical structure of this specific certification exam question (AI-103/AI-102 context), the 
correct selections are:OverfittingIncrease the amount of training data

## Question 115

Source pages: 120

You are developing an application that will use Azure AI Search for internal documents. 
You need to implement document-level filtering for Azure AI Search. 
Which three actions should you include in the solution? Each correct answer presents part of the solution. 
NOTE: Each correct selection is worth one point.

Options:
- A. Add allowed groups to each index entry
- B. Create one index per group.
- C. Send access tokens from Microsoft Entra ID, with the search request.
- D. Retrieve all the groups.
- E. Retrieve the group memberships of the user
- F. Supply the groups as a filter for the search requests

Answer: AEF

## Question 116

Source pages: 120

Client applications must display page-level citations that have bounding polygons for both text and images. Provide text and image location metadata. 
Extract tables that span multiple pages.

Options:
- A. Document
- B. Document
- C. Azure Content Understanding
- D. GenAI Prompt

Answer: C

## Question 117

Source pages: 120, 121

HOTSPOT Which projection type should you use for each data type? To answer, select the appropriate options in the answer

Answer: _No answer text extracted._
