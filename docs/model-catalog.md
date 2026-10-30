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
| DeepSeek | DeepSeek V4.1 Flash | Open | mit | 552B / 8B–16B active | MoE | [Source](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | Official model card: 552B backbone; active parameters vary by inference mode (8B / 16B). Not the earlier V4 Flash 284B/13B model. Original September 2026 V4.1 checkpoint; the active deepseek-flash API alias moved to the October 17, 2026 update. |
| DeepSeek | DeepSeek V4.1 Flash 1017 | Open | mit | 552B / 8B–16B active | Causal Encoder-Decoder MoE | [Source](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | October 17, 2026 minor version update. 552B denotes officially reported backbone size for V4.1, with 8B activated for prefill and 16B for decode. Hugging Face also lists 763B model-tensor parameters (different counting basis). Updated weights have been published; official API deepseek-flash serves this revision at unchanged prices. |
| GLM / Z.AI | GLM-5 | Open | mit | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5) | Official model card states 744B/40B (backbone). Some repositories show ~754B including extra tensors. |
| GLM / Z.AI | GLM-5-Turbo | Closed | Not verified | Not disclosed | Not disclosed | — | Z.AI says GLM-5 Turbo was trained/optimized specifically for OpenClaw agents and tool use, and is faster. It has not confirmed that Turbo uses the same checkpoint as publicly released GLM-5.; No matching public GLM-5-Turbo checkpoint verified. Open GLM-5 does not prove this variant is open. |
| GLM / Z.AI | GLM-5.1 | Open | mit | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.1) | Uses GLM-5-class 744B/40B backbone; GLM-5.3 documentation says same base as GLM-5.2. Totals including auxiliary layers may differ. |
| GLM / Z.AI | GLM-5.2 | Open | mit | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.2) | Uses GLM-5-class 744B/40B backbone; GLM-5.3 documentation says same base as GLM-5.2. Totals including auxiliary layers may differ. |
| GLM / Z.AI | GLM-5.3 | Open | glm-5.3 | 744B / 40B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.3) | Uses GLM-5-class 744B/40B backbone; GLM-5.3 documentation says same base as GLM-5.2. Totals including auxiliary layers may differ. |
| GLM / Z.AI | GLM-5.3-Flash | Open | mit | 320B / 18B active | MoE | [Source](https://huggingface.co/zai-org/GLM-5.3-Flash) | Public model; 320B / 18B active according to official card. |
| Google | Gemini 3.1 Flash-Lite | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.1 Pro Preview | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.5 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | Deprecated October 8, 2026. API calls automatically route to gemini-3.6-flash; no longer a separately selectable model. |
| Google | Gemini 3.5 Flash-Lite | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.6 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 3.7 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | Deprecated October 8, 2026. API calls automatically route to gemini-3.8-flash; no longer a separately selectable model. |
| Google | Gemini 3.8 Flash | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Google | Gemini 4 Argon | Closed | Not verified | Not disclosed | Sparse MoE | — | Google confirms a Sparse MoE design but has not disclosed total or activated parameters.; No downloadable Gemini 4 Argon model files published. |
| Kimi | Kimi K2.6 | Open | modified-mit | 1T / 32B active | MoE | [Source](https://huggingface.co/moonshotai/Kimi-K2.6) | Official Kimi K2.6 checkpoint: 1T total / 32B active. |
| Kimi | Kimi K2.7 Code | Open | modified-mit | 1T / 32B active | MoE | [Source](https://huggingface.co/moonshotai/Kimi-K2.7-Code) | Official Kimi K2.7 Code checkpoint: 1T total / 32B active. |
| Kimi | Kimi K2.7 Code Highspeed | Open | modified-mit | 1T / 32B active | MoE | [Source](https://huggingface.co/moonshotai/Kimi-K2.7-Code) | Kimi confirms HighSpeed is the same K2.7 Code model, served roughly 5–6× faster (https://www.kimi.com/code/docs/en/kimi-code/whats-new.html). |
| Kimi | Kimi K3 | Open | kimi-k3 | 2.8T / 104B active | MoE | [Source](https://huggingface.co/moonshotai/Kimi-K3) | — |
| Kimi | Kimi K3.1 Pro | Closed | Not verified | 2.8T / 104B active | Multimodal MoE | [Source](https://www.kimi.com/en/blog/kimi-k3-1-pro) | Kimi officially describes a 2.8T-total / 104B-active multimodal MoE, with a 1M-token context. The API is live. Downloadable K3.1 Pro weights are promised by November 4, 2026, but have NOT been released as of October 24.; Planned public weights release by November 4, 2026. Until downloadable K3.1 Pro weights actually appear, keep Closed. Open Kimi K3 weights are a different checkpoint. |
| Kimi | Kimi K3.1 Pro Highspeed | Closed | Not verified | 2.8T / 104B active | Multimodal MoE | [Source](https://www.kimi.com/en/blog/kimi-k3-1-pro) | Same K3.1 Pro model as the standard tier, served 2–3x faster; 2.8T total / 104B active, 1M context. Cache-hit price is unchanged.; K3.1 Pro downloadable checkpoint is not yet released; a faster serving tier does not make an unreleased model Open. |
| Meta | Muse Wonder | Closed | Not verified | Not disclosed | Not disclosed | — | 1M context. Standard Meta Model API and OpenRouter availability. Parameter counts undisclosed.; Public API, but no downloadable model checkpoint verified. |
| Meta | Muse Wonder Full | Closed | Not verified | Not disclosed | Not disclosed | — | 1M context. Muse Code Power or Maximum Usage subscription only; no public per-token API price.; Subscription-only Muse Code offering. No public downloadable checkpoint verified. |
| Meta / OpenRouter | Muse Glimmer 30B | Open | Not verified | 30B | Dense | [Source](https://openrouter.ai/meta/muse-glimmer-30b) | — |
| Meta / OpenRouter | Muse Spark 1.1 | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Meta / OpenRouter | Muse Spark 1.2 | Closed | Not verified | Not disclosed | Not disclosed | — | Muse Spark Open is not explicitly a public release of the hosted 1.2 checkpoint. |
| Meta / OpenRouter | Muse Spark 1.2 Contributor | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Meta / OpenRouter | Muse Spark 1.3 | Closed | Not verified | Not disclosed | Not disclosed | — | Meta confirms Muse Spark Open shares the base model with hosted 1.3, but uses additional safety post-training, so the hosted 1.3 checkpoint is not verified identical. |
| Meta / OpenRouter | Muse Spark 1.3 Contributor | Closed | Not verified | Not disclosed | Not disclosed | — | — |
| Meta / OpenRouter | Muse Spark Open | Open | muse-model-license | 816B / 42B active | Multimodal MoE | [Source](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) | Meta released Muse Spark Open on October 15 with its own Muse Model License and additional safety post-training. It shares the base model with hosted Muse Spark 1.3, but is not a verified identical checkpoint for hosted Spark 1.2 or 1.3. |
| MiniMax | MiniMax M2.7 | Open | non-commercial | 230B / 10B active | MoE | [Source](https://developer.nvidia.com/blog/minimax-m2-7-advances-scalable-agentic-workflows-on-nvidia-platforms-for-complex-ai-applications) | Weights published at MiniMaxAI/MiniMax-M2.7. Model license restricts commercial use unless MiniMax grants prior written authorization. 230B/10B MoE, 200K-class context. |
| MiniMax | MiniMax M2.7 Highspeed | Open | non-commercial | 230B / 10B active | MoE | [Source](https://developer.nvidia.com/blog/minimax-m2-7-advances-scalable-agentic-workflows-on-nvidia-platforms-for-complex-ai-applications) | Same M2.7 model, served faster. MiniMax official product page explicitly says standard and Highspeed have identical results; no separate Highspeed checkpoint needed. |
| MiniMax | MiniMax M3 | Open | minimax-community | 428B / 23B active | MoE | [Source](https://huggingface.co/MiniMaxAI/MiniMax-M3) | Native text/image/video-input MoE model, sparse attention, ~1M context. Weights released June 12, 2026; MiniMax Community License, not a standard permissive OSI license. |
| MiniMax | MiniMax M3.1 Flash | Open | minimax-community | 428B / 23B active | Multimodal MoE | [Source](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | Official downloadable model files now exist; MiniMax's earlier October 19 launch article stated weights would follow. 428B total / 23B active MoE with sparse attention, 1M context and native image/video inputs. Custom MiniMax Community License, not MIT/Apache 2.0. |
| Mistral | Mistral Large 4 | Open | mistral-ecosystem-open-weight-v26.10 | 1.05T / 52B active | Multimodal MoE | [Source](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | Official FP8 and NVFP4 checkpoints published October 29, 2026. 1.05T total / 52B active including embeddings and output layers (49B core-active); separate 1.6B vision encoder. License allows general commercial use, but hosted model-as-a-service businesses need a separate Mistral license. |
| Mistral | Mistral Medium 3.5 | Open | modified-mit | 128B / 128B active | Dense | [Source](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) | Official Mistral release: 128B dense model, 256K context. Public downloadable checkpoint under Modified MIT; license includes extra conditions for high-revenue businesses. |
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
| OpenAI | GPT-6.1 Terra | Closed | Not verified | Not disclosed | Not disclosed | — | Parameters not publicly disclosed. 1.05M context window, 128K maximum output; text/image input and text output. Released October 26, 2026.; No downloadable GPT-6.1 Terra checkpoint publicly released. |
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
