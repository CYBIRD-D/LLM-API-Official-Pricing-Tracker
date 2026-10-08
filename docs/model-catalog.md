# Model Openness, Licenses and Parameters

Generated from [`data/models.json`](../data/models.json). **Open** = matching downloadable model checkpoint; **Closed** = no matching public checkpoint verified. These labels do not indicate whether a license is OSI-approved.

| Provider | Model | Open/Closed | License | Parameters (total / active) | Architecture | Evidence | Notes |
|---|---|---|---|---|---|---|---|
| Anthropic | Claude Fable 5 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Fable 5.1 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Haiku 5.5 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Opus 4.7 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Opus 4.8 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Opus 5 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Opus 5.5 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Sonnet 4.6 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Sonnet 5 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Anthropic | Claude Sonnet 5.5 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| DeepSeek | DeepSeek V4 Pro | Open | mit | 1.6T / 49B active | MoE | [Source](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | Official V4 Pro post-trained checkpoint is downloadable. |
| DeepSeek | DeepSeek V4.1 Flash | Open | mit | 552B / 8B–16B active | MoE | [Source](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | Official model card: 552B backbone; active parameters vary by inference mode (8B / 16B). Not the earlier V4 Flash 284B/13B model. |
| GLM / Z.AI | GLM-5 | Open | mit | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5) | Official model card states 744B/40B (backbone). Some repositories show ~754B including extra tensors. |
| GLM / Z.AI | GLM-5-Turbo | Closed | Not verified | Not disclosed | Not disclosed | [Source](https://docs.z.ai/guides/overview/pricing) | GLM-5 base is public, but Turbo is a separately named hosted SKU with no verified corresponding Turbo checkpoint.; Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| GLM / Z.AI | GLM-5.1 | Open | mit | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.1) | Uses GLM-5-class 744B/40B backbone; GLM-5.3 documentation says same base as GLM-5.2. Totals including auxiliary layers may differ. |
| GLM / Z.AI | GLM-5.2 | Open | mit | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.2) | Uses GLM-5-class 744B/40B backbone; GLM-5.3 documentation says same base as GLM-5.2. Totals including auxiliary layers may differ. |
| GLM / Z.AI | GLM-5.3 | Open | glm-5.3 | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.3) | Uses GLM-5-class 744B/40B backbone; GLM-5.3 documentation says same base as GLM-5.2. Totals including auxiliary layers may differ. |
| GLM / Z.AI | GLM-5.3-Flash | Open | mit | 320B / 18B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.3-Flash) | Public model; 320B / 18B active according to official card. |
| Google | Gemini 3.1 Flash-Lite | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.1 Pro Preview | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.5 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.5 Flash-Lite | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.6 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.7 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.8 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Kimi | Kimi K2.6 | Closed | Not verified | Not disclosed | Not disclosed | — | Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Kimi | Kimi K2.7 Code | Closed | Not verified | Not disclosed | Not disclosed | — | Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Kimi | Kimi K2.7 Code Highspeed | Closed | Not verified | Not disclosed | Not disclosed | — | Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Kimi | Kimi K3 | Open | kimi-k3 | 2.8T / 104B active | MoE | [Source](https://huggingface.co/moonshotai/Kimi-K3) | — |
| Meta / OpenRouter | Muse Glimmer 30B | Open | Not verified | 30B | Dense | [Source](https://openrouter.ai/meta/muse-glimmer-30b) | — |
| Meta / OpenRouter | Muse Spark 1.1 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Meta / OpenRouter | Muse Spark 1.2 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Meta / OpenRouter | Muse Spark 1.2 Contributor | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Meta / OpenRouter | Muse Spark 1.3 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Meta / OpenRouter | Muse Spark 1.3 Contributor | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Mistral | Mistral Large 4 | Closed | Not verified | 1.05T / 49B active | MoE | [Source](https://huggingface.co/mistralai/Mistral-Large-4.0-1T05-A52B) | Weights planned Oct 31, 2026; 49B core activated, ~52B including embeddings / output layers.; Release of public checkpoint announced but not verified as downloadable by the data cutoff. |
| Mistral | Mistral Medium 3.5 | Closed | Not verified | Not disclosed | Not disclosed | — | Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Mistral | Mistral Small 4 | Open | apache-2.0 | 119B / 6.5B active | MoE | [Source](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | — |
| OpenAI | GPT-5.4 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.4 mini | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.4 nano | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.4 Pro | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.5 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.5 Pro | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.6 Luna | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.6 Sol | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-5.6 Terra | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-6 Astra | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-6 Luna | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-6 Sol | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| OpenAI | GPT-6.1 Sol | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Qwen | Qwen3.5 Flash | Open | apache-2.0 | 35B / 3B active | MoE | [Source](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) | Qwen model card explicitly maps hosted Qwen3.5-Flash to public Qwen3.5-35B-A3B; hosted API has added tools/context. |
| Qwen | Qwen3.5 Plus | Open | apache-2.0 | 397B / 17B active | MoE | [Source](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | Alibaba explicitly maps hosted Qwen3.5-Plus to public Qwen3.5-397B-A17B; API differs in built-in features. |
| Qwen | Qwen3.6 Flash | Open | apache-2.0 | 35B / 3B active | MoE | [Source](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) | Alibaba announcement directly identifies open Qwen3.6-35B-A3B as the model to call using the Qwen3.6-Flash API name; API may differ. |
| Qwen | Qwen3.6 Plus | Closed | Not verified | Not disclosed | Not disclosed | [Source](https://huggingface.co/Qwen/collections) | Public Qwen3.6 35B/27B variants do not automatically establish a release of the hosted Plus checkpoint.; Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Qwen | Qwen3.7 Flash | Closed | Not verified | Not disclosed | Not disclosed | [Source](https://www.alibabacloud.com/help/en/model-studio/qwen3-7-flash) | Alibaba API listing verified; no directly corresponding 3.7 Flash downloadable model identified.; Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Qwen | Qwen3.7 Max | Closed | Not verified | Not disclosed | Not disclosed | [Source](https://docs.qwencloud.com/developer-guides/getting-started/vision-models) | API model listed; corresponding downloadable 3.7 Max checkpoint not verified.; Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Qwen | Qwen3.7 Plus | Closed | Not verified | 397B / 17B active | MoE | [Source](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | Qwen official comparison table reports 397B/17B for Qwen3.7-Plus; no matching public Qwen3.7-Plus checkpoint verified. NOT the 3.5 release.; Corresponding publicly downloadable checkpoint not verified; not proof a proprietary architecture. |
| Qwen | Qwen3.8 Flash | Open | qwen-community-1.0 | 125B / 6B active | MoE | [Source](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | Official model card: API Qwen3.8-Flash is based on public Flash-Next. 125B is LM core, with additional 51B n-gram embeddings and 4B MTP; production API adds features. |
| Qwen | Qwen3.8 Max | Open | qwen3.8-max | 2.4T / 95B active | MoE | [Source](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | Qwen official checkpoint now downloadable; API adds vision, non-thinking mode, 1M default context and tools. |
| xAI | Grok 4.20 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| xAI | Grok 4.3 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| xAI | Grok 4.5 | Closed | Not verified | ≈1.5T (Musk claim) | Not disclosed | [Source](https://x.com/elonmusk/status/2078289996323148076) | Approximate scale claimed by Elon Musk on X; not specified or independently verified in xAI model documentation. 4.5/4.6 1.5T, 4.7 2.1T.; Public model weights unavailable; parameter number is an unverified founder statement. |
| xAI | Grok 4.6 | Closed | Not verified | ≈1.5T (Musk claim) | Not disclosed | [Source](https://x.com/elonmusk/status/2082123925283041545) | Approximate scale claimed by Elon Musk on X; not specified or independently verified in xAI model documentation. 4.5/4.6 1.5T, 4.7 2.1T.; Public model weights unavailable; parameter number is an unverified founder statement. |
| xAI | Grok 4.7 | Closed | Not verified | ≈2.1T (Musk claim) | Not disclosed | [Source](https://x.com/elonmusk/status/2082123925283041545) | Approximate scale claimed by Elon Musk on X; not specified or independently verified in xAI model documentation. 4.5/4.6 1.5T, 4.7 2.1T.; Public model weights unavailable; parameter number is an unverified founder statement. |
| xAI | Grok Build 0.1 | Closed | Not verified | Not disclosed | Not disclosed | — | — |

**Caution:** A branded hosted API may have extra tools/context or post-training changes relative to a corresponding released checkpoint. Founder-claimed figures are not independently verified. See [methodology](methodology.md).
