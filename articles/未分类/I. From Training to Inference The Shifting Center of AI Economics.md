---
title: "I. From Training to Inference: The Shifting Center of AI Economics"
source: "https://www.acecamptech.com/article/detail/70559507"
category: "未分类"
date: "2026/02/25 23:21"
downloaded: "2026-03-22 20:14:59 JST"
---

# I. From Training to Inference: The Shifting Center of AI Economics

The Next Decade for GPUs Is Not Training, But Inference — Can AMD Seize the Moment?

Chinese

EN

The Next Decade for GPUs Is Not Training, But Inference — Can AMD Seize the Moment?

VIPOriginalIndustry：TMT, Semiconductor, ​Manufacturing, AI

2026/03/11 05:15:46

Views 14400

Likes 0

Quick-Q

Summary

1. The AI industry's center of gravity is shifting from training to inference, with inference TAM rapidly surpassing training;
2. A comprehensive hardware comparison between AMD MI450/Helios and Nvidia Vera Rubin NVL144 on TCO, memory capacity, and rack-scale architecture;
3. ROCm's software composability gap, supply chain bottlenecks in CoWoS and HBM4, and the structural threat from custom ASICs.

The full text is 5653 words, estimated reading time 12 minutes

VIP Free

The AI industry's center of gravity is shifting from training to inference. Training is a one-time capital expenditure; inference is a 24/7 utility bill -- when Gemini processes 10 billion tokens per minute and Advantage+ runs on $60 billion in annualized ad spend, the economics of inference compute become a more critical decision variable than peak training throughput.

The core thesis of this report is that the competitive rules for the inference market are fundamentally different from training. **Training is about "who has the largest cluster"; inference is about "who delivers the lowest cost per token."** Under this framework, the memory wall, TCO, rack-scale architecture, and software ecosystem collectively determine winners -- not single-card benchmarks. Current industry projections suggest that AMD's MI450/Helios combination demonstrates theoretical competitiveness in hardware TCO. However, realizing this advantage faces two key uncertainties: first, whether ROCm's composability gaps can be closed; second, the actual production timeline for its rack-scale systems remains contested within the industry. The optimistic view points to H2 2026, but supply chain intelligence suggests that manufacturing and advanced packaging challenges could push large-scale commercial delivery to Q2 2027. If both hardware and software land later than expected, theoretical hardware advantages may fail to translate into real-world deployment wins.

# --- **I. From Training to Inference: The Shifting Center of AI Economics**

An intuitive comparison: training a GPT-4-class model may cost hundreds of millions of dollars, but that expense is incurred once; inference -- serving billions of users daily with answers, code generation, and ad ranking -- is a 24/7 process of burning electricity, and one year of inference costs can far exceed a single training run.

Alphabet's Q4 2025 earnings data shows Gemini App has over 750 million MAUs, with first-party models processing over 10 billion tokens per minute via API calls. All these inference requests run on Google's TPU and GPU clusters, with each API call stacking electricity and hardware depreciation costs. Meta's Advantage+ ad system follows the same logic: $60 billion in annualized ad spend translates to billions of inference calls per day -- every ad ranking requires the model to complete inference within milliseconds.

This structural shift has a clear implication for the GPU market: **the inference TAM is rapidly surpassing the training TAM**. Training demand is concentrated among a handful of frontier labs (OpenAI, Google DeepMind, Anthropic, Meta FAIR); inference demand is distributed across every application and service that has deployed AI capabilities. When inference becomes the primary battleground, the competitive rules change accordingly -- training is about "who has the largest cluster"; inference is about "who delivers the lowest cost per token, lowest latency, and highest throughput."

# --- **II. Memory Wall: In the Inference Regime, Memory Is King**

Why does memory matter more than compute in inference? Because **the bottleneck in LLM inference is not computation itself, but the speed at which model parameters can be moved from memory to compute units.**

A simple physical constraint: a 600-billion-parameter MoE (Mixture of Experts) model, even with FP4 quantization (0.5 bytes per parameter), still requires approximately 300GB of memory for model weights alone. During inference, the KV cache (key-value cache, storing intermediate states of previously processed tokens) consumes additional memory -- larger batch sizes and longer contexts cause the KV cache to balloon. When memory runs out, the options are either reducing batch size (lowering throughput) or sharding the model across multiple GPUs (increasing communication overhead) -- both raise the cost per token.

This is why HBM capacity and bandwidth are so critical to inference economics. According to AMD's official disclosures and CES 2026 presentation, the Helios rack houses 72 MI455X GPUs, each equipped with 432GB of HBM4 memory, for a total rack HBM4 capacity of approximately 31TB and aggregate memory bandwidth of 1.4PB/s. For comparison, based on Nvidia's GTC 2025 official disclosures and The Register's detailed teardown of the CES 2026 presentation, Vera Rubin NVL144 features 288GB HBM4 per GPU, with 72 modules totaling approximately 20.7TB of HBM4, and total fast storage (including HBM4 + LPDDR) of 75TB. Notably, Nvidia upgraded the Rubin GPU's per-die HBM4 bandwidth from the originally announced 13TB/s to 22TB/s at CES 2026, achieved entirely through silicon process improvements without relying on compression. This is clearly an attempt to compensate for its absolute capacity disadvantage through extremely high data throughput.

AMD leads by approximately 50% in HBM4 memory capacity (31TB vs 20.7TB) -- consistent with AMD's own comparative data presented at the June 2025 Advancing AI event (where AMD claimed "50 percent higher memory capacity"). A 50% capacity lead is not a marginal gap -- it directly determines that the same ultra-large model can run with larger batch sizes and accommodate longer contexts on AMD racks, thereby reducing inference cost per token. In inference workloads, memory capacity and bandwidth are typically the bottleneck, not compute -- meaning AMD's memory advantage may carry more weight in real-world inference TCO than Nvidia's lead in FP4 peak throughput.

# --- **III. Helios vs NVL144: A Head-to-Head Rack-Scale Showdown**

When the unit of competition shifts from individual GPUs to entire racks, every architectural decision affects TCO. The following comparison is based on official disclosures from each company and cross-referenced with multiple independent sources.

AMD Helios core specs: 72 MI455X GPUs (CDNA 5 architecture, TSMC 2nm/3nm hybrid chiplet process), paired with sixth-generation EPYC CPUs codenamed "Venice" (Zen 6 architecture, up to 256 cores, 1.6TB/s memory bandwidth per socket), intra-rack GPU scale-up interconnect bandwidth up to 260TB/s (UALink 1.0, per AMD), Ethernet scale-out bandwidth of approximately 43TB/s, rack requiring liquid cooling at the hundred-kilowatt level (AMD confirmed rear-door liquid cooling and open rack standards; precise power figures not officially disclosed).

Vera Rubin NVL144 benchmark specs: 72 dual-die GPU modules (144 GPU dies total, Rubin architecture, TSMC 3nm), paired with custom 88-core ARM CPUs codenamed "Vera," intra-rack interconnect via NVLink 6.0 + NVSwitch. Per The Register's teardown of the CES 2026 Rubin rack, the NVL72 configuration provides approximately 260TB/s of NVLink intra-rack bandwidth; NVL144 interconnect bandwidth has not been separately disclosed by Nvidia and is estimated to be higher. Rack power consumption is estimated by third parties at approximately 120-130kW.

![](https://image.acecamptech.com/article_image/50523361/0.7486315912339582.png)

**Key findings:**

Nvidia leads by approximately 24% in FP4 inference throughput (3.6 vs 2.9 exaFLOPS), but AMD leads by approximately 17% in FP8 training throughput (1.4 vs 1.2 exaFLOPS). AMD leads by approximately 50% in HBM4 capacity, which has direct economic value for memory-bound inference workloads. AMD and Nvidia are at comparable levels for intra-rack scale-up interconnect bandwidth (both at 260TB/s), but with fundamentally different underlying technologies: Nvidia uses its proprietary NVLink 6.0 + NVSwitch fully connected topology, while AMD uses the open UALink 1.0 standard via Broadcom Tomahawk 6 Ethernet switching. The real-world communication efficiency differences between these two approaches (e.g., latency and effective bandwidth in fully connected vs switched topologies) in multi-GPU collaborative training still await third-party benchmark validation.

A noteworthy process node divergence: MI455X uses TSMC 2nm/3nm hybrid chiplet technology, while Vera Rubin uses 3nm -- AMD is partially one generation ahead in process node. According to TSMC's published data, 2nm delivers approximately 20-30% energy efficiency improvement, but 2nm is a brand-new node with higher yield risk than mature 3nm. If early yields fall short, AMD's delivery cadence and cost control will be severely impacted. In fact, more pessimistic projections have already emerged within the supply chain. Intelligence suggests that AMD's rack system benchmarked against NVL72 is encountering manufacturing and advanced packaging delays, and that commercially meaningful volume ramp could be pushed back to Q2 2027. It must be emphasized that these remain market speculation, not official determinations. But if this scenario materializes, AMD would face an extremely challenging competitive mismatch: it may need to compete directly against Nvidia's planned next-generation Rubin Ultra architecture in 2027, bearing enormous generational pressure.

---

# **IV. TCO: The Ultimate Yardstick for the Inference Market**

**In inference workloads, TCO breaks down into: hardware procurement costs (GPU + CPU + networking + rack), electricity costs (power consumption x electricity price x uptime), cooling costs, and software efficiency (how much effective inference the same hardware can deliver).**

According to SemiAnalysis estimates, at FP6 precision commonly used for LLM inference, AMD MI450 delivers approximately 68% lower TCO per PFLOPS compared to Nvidia's Vera Rubin 200; at FP8 precision, the advantage is approximately 38%. Combined with the energy efficiency gains from 2nm process technology, MI450's TCO competitiveness in inference scenarios is significant.

**A critical caveat: TCO advantage does not equal deployment advantage.** TCO calculations reflect the theoretical optimum, but in real-world deployments, software stack maturity directly impacts hardware utilization -- if software underperforms, hardware that is theoretically 30% cheaper may only achieve 70% efficiency, erasing the TCO advantage entirely. This is precisely the question the next section addresses.

---

# **V. ROCm's Composability Deficit: Hardware Wins, Software Lags Behind**

According to SemiAnalysis's InferenceX v2 benchmark report published on February 15, 2026 -- the most comprehensive AI inference benchmark to date -- AMD MI355X (the predecessor to MI450, CDNA 4 architecture) matched or even exceeded Nvidia's B200 in FP8 single-node aggregate inference. However, **when three frontier inference optimizations -- FP4 precision, disaggregated prefill, and wide expert parallelism -- were simultaneously enabled, AMD's performance fell significantly behind.**

**The root cause is composability:** AMD's ROCm software stack can implement FP4, disaggregated prefill, and wide EP individually, but performance degrades sharply when all three are enabled simultaneously. SemiAnalysis was blunt: "Software continues to be a massive bottleneck for AMD GPUs." SemiAnalysis also disclosed that a focused composability effort would launch in full in H1 2026, making this the critical window for ROCm to close the gap before MI450 reaches volume production.

ROCm 7.2, released in January 2026, added FP8/FP4 support in rocMLIR and MIGraphX, GEMM kernel optimizations for MI355X, and GDA (Global Data Allocation) topology-aware communication optimization. These improvements are directionally correct, but still fall short of the production-grade standard of "three optimizations running simultaneously without performance penalties."

The investment implication is clear: MI450's hardware TCO advantage objectively exists, but whether it translates into real inference deployments depends on whether ROCm achieves composability maturity by H2 2026. If Q3/Q4 2026 third-party benchmarks show AMD closing the gap in FP4 + disagg + wide EP scenarios, it would be a major catalyst for AMD's stock; conversely, if the gap persists, hyperscalers may allocate more inference budgets to Nvidia or pivot to custom ASICs.

---

# **VI. EPYC Venice: The Underestimated "Bundling" Synergy**

6GW of AI racks require more than GPUs. Every server needs a CPU as the host node to manage data flows, run scheduling logic, and handle non-GPU workloads. AMD's Helios rack is paired with the sixth-generation EPYC CPU, codenamed "Venice."

Public information shows EPYC Venice is based on the Zen 6 architecture, with up to 256 cores (Zen 6c), TSMC 2nm process, memory bandwidth per socket upgraded to 1.6TB/s (approximately 2.6x the current Turin's 614GB/s), up to 70% performance improvement over the previous generation, and higher CPU-to-GPU transfer bandwidth optimized for the Helios rack.

Q4 2025 data shows AMD's server CPU revenue share climbed to a record 41.3% (up 4.9 percentage points YoY), with unit share at 28.8% (up 3.1 percentage points YoY). Revenue growing significantly faster than units indicates AMD is selling fewer chips at higher ASPs -- each EPYC 9005 series chip commands an ASP far above Intel's Xeon. Intel still holds 71.2% unit share and 58.7% revenue share, but the trend is clear: AMD is rapidly gaining ground in the high-end market.

When Helios bundles EPYC and Instinct GPUs, AMD is effectively using massive GPU orders to drive CPU share -- an underappreciated synergy. Each GW-class GPU order simultaneously represents tens of thousands of EPYC units, and Venice's 1.6TB/s memory bandwidth is purpose-built for AI racks. This depth of CPU + GPU integration is something Nvidia currently cannot replicate (Nvidia has no server CPU product line; the Vera CPU is a custom 88-core ARM chip designed for NVL144, not sold independently).

---

# **VII. Supply Chain Chokepoints: The Bottleneck of CoWoS Packaging and HBM4**

MI450's delivery depends not only on AMD's design capabilities, but also on whether two critical supply chain nodes can be unlocked.

**The first is TSMC's CoWoS advanced packaging.** Research indicates AMD's 2026 CoWoS allocation accounts for approximately 11% of global capacity (approximately 80K wafers), while Nvidia takes approximately 60% (approximately 510K wafers), and Broadcom (including Google TPU and Meta MTIA foundry work) accounts for approximately 15%. AMD's MI450 will transition from CoWoS-S to CoWoS-L packaging, representing a new process node switch. Recent industry speculation about potential delays to the MI450 series until 2027 is primarily grounded in concerns over early CoWoS-L yield rates and capacity ramp difficulties. The yield ramp curve is a dynamic process, making the final production timeline inherently based on evolving projections.

**The second is HBM4 supply.** Multiple media reports indicate Samsung Electronics will be the primary HBM4 supplier for AMD's MI450 -- diverging from Nvidia's primary reliance on SK Hynix for HBM. Samsung's yields and performance lagged behind SK Hynix during the HBM3e era, and whether HBM4 can meet quality and delivery cadence targets directly affects MI450's production timeline.

TSMC, as the sole large-scale CoWoS supplier, holds pricing power over all AI chip customers: whether AMD, Nvidia, or Google TPU prevails, all must use TSMC's packaging lines. Regardless of which GPU vendor gains share, the scarcity of CoWoS capacity persists. This represents the purest "picks and shovels" thesis in the AI industry.

---

# **VIII. Custom ASICs: The Largest Structural Risk Hanging Over GPU Vendors**

The inference market's competitors extend beyond AMD and Nvidia -- hyperscalers are increasingly serious about developing their own chips, while highly specialized inference accelerators such as LPUs are maturing.

The threat logic of ASICs against merchant GPU inference is straightforward: the more standardized hyperscaler inference workloads become (e.g., all running Transformer inference), the greater the economic advantage of custom ASICs -- because ASICs can be tailored to specific workloads without the redundant transistors required for general-purpose GPU computing.

**Hyperscaler landscape overview:**

**Google TPU:** According to a November 2025 CNBC in-depth report, Google TPUs are operating at full capacity, continuously handling the massive inference demands of Gemini and other first-party models.

**Amazon Trainium:** Amazon has deployed 500,000 Trainium2 chips in its AI data centers for Anthropic's model training. Amazon's chief chip architect stated that Trainium delivers 30-40% better price-performance than other hardware providers on AWS.

**Microsoft Maia:** Microsoft released the Maia 200 chip on January 26, 2026, claiming it surpasses Google TPU and Amazon Trainium across multiple metrics.

**Meta MTIA:** Meta is on the same trajectory. Its second-generation MTIA (codenamed "Artemis," TSMC 5nm) was deployed for recommendation model inference in 2025. Per TrendForce's January 30, 2026 report, the third-generation MTIA will use TSMC 3nm + GUC packaging, with an expected H2 2026 launch.

For AMD, MI450 faces competition not only from Nvidia, but also from Google TPU, Amazon Trainium, Microsoft Maia, Meta MTIA, as well as LPUs and custom ASICs manufactured by Broadcom/Marvell -- the competitive landscape is far more complex than the simplified "AMD vs Nvidia" narrative.

---

# **IX. Verifiable Milestones**

The above analysis can be distilled into four key variables requiring validation between H2 2026 and 2027:

**1) ROCm composability:** Whether InferenceX or equivalent third-party benchmarks show AMD matching Nvidia in FP4 + disagg + wide EP scenarios. If achieved, MI450's TCO narrative holds; if not, hardware advantages will be discounted by software.

**2) 2nm yield and CoWoS-L ramp:** MI455X is among TSMC's first high-volume 2nm customers, with yield data becoming clearer through H2 2026. CoWoS-L capacity ramp proceeds in parallel, compounding both variables. These two indicators directly determine whether the product ships on schedule in H2 2026 or is delayed to 2027 as pessimistic projections suggest.

**3) Samsung HBM4 quality:** Whether Samsung can achieve quality and delivery stability comparable to SK Hynix's HBM3e directly impacts MI450's production cadence.

**4) ASIC substitution pace:** The actual deployment scale and inference TCO of the latest Google TPU generation, Amazon Trainium3, Microsoft Maia 200, and Meta MTIA-3 will determine how the boundary between "merchant GPU vs custom ASIC" shifts.

---

# **Conclusion**

The inference market is the next major battleground for AI compute, with the competitive rules shifting from "who has the largest cluster" to "who delivers the lowest cost per token." AMD MI450/Helios demonstrates notable competitiveness against Nvidia's Vera Rubin at the hardware level: HBM4 capacity leads by approximately 50% (31TB vs 20.7TB), FP8 training throughput leads by approximately 17% (1.4 vs 1.2 exaFLOPS), and 2nm process delivers energy efficiency advantages; Nvidia maintains its lead in FP4 inference throughput (+24%), while both are at comparable levels for intra-rack scale-up interconnect bandwidth (both at 260TB/s, but with different technical paths -- NVLink fully connected vs UALink switched topology, with real-world efficiency differences yet to be validated). Each side has structural strengths, and outcomes depend on specific workloads.

However, the ultimate arbiter of inference economics is not a hardware spec sheet, but the product of "hardware advantage x software maturity." ROCm's composability deficit is the single largest uncertainty -- it determines whether MI450 is "cheaper and larger on paper" or "genuinely cheaper and larger in actual deployments." Meanwhile, the rise of custom ASICs is structurally shrinking the GPU TAM -- Meta MTIA-3, next-generation Google TPU, and Amazon Trainium3 are all launching in H2 2026, posing a genuine substitution threat to merchant GPUs.

**For investors, H2 2026 through H1 2027 represents a high-risk validation window where all core projections converge.** Several still-unresolved variables demand close monitoring: Will MI450 rack systems achieve initial shipments in H2 2026, or will they be delayed to Q2 2027 as pessimistic projections suggest? Can ROCm's composability challenges be overcome on schedule? Any disruption to expected timelines would re-price AMD's share in the AI inference market. The current inference economics ledger is largely built on technical specifications and theoretical projections published by both sides; the real verdict still rests with a semiconductor supply chain full of unknowns.

**The above content does not constitute any investment advice. Invest at your own risk.**

Follow-up

[If AMD's MI450 is delayed to 2027 due to CoWoS-L yields, will its HBM4 capacity advantage be fully offset by Nvidia's Rubin Ultra?](/chat?title=If%20AMD's%20MI450%20is%20delayed%20to%202027%20due%20to%20CoWoS-L%20yields,%20will%20its%20HBM4%20capacity%20advantage%20be%20fully%20offset%20by%20Nvidia's%20Rubin%20Ultra?) [Assuming ROCm composability issues persist in 26H2, will hyperscalers cut AMD orders and accelerate the shift to custom ASICs like TPU/Trainium?](/chat?title=Assuming%20ROCm%20composability%20issues%20persist%20in%2026H2,%20will%20hyperscalers%20cut%20AMD%20orders%20and%20accelerate%20the%20shift%20to%20custom%20ASICs%20like%20TPU/Trainium?)

AI推理GPUCOWOS算力HBM

Likes

Dislikes

3

Share

[![](https://image.acecamptech.com/avatar/50523361/0.16602141984665542.jpg?x-oss-process=style/avatar)](/organizer/20509829)

[笃研究 ResearchD](/organizer/20509829)

Acecamp analyst

Follow

笃研究由9名投资研究专业人士组成。团队多名成员具有超过10年的头部买方或国际投行投资与研究工作经验。
团队牵头人具有20年境内外市场投资与研究经验，曾获Institutional Investor亚洲区(除日本)大宗商品分析师第一名、中国能源行业第一名，Asiamoney A股/港股材料、能源、交通行业分析师第一名。
我们的共同愿景是更加快速、自由地向市场传达独立的分析观点，提供有别于大型机构基于各种考虑而扭曲变形的研究产品。
ResearchD is composed of 9 investment research professionals. Multiple team members bring over 10 years of investment and research experience at leading buy-side institutions or bulge bracket banks.
The team leader has 20 years of investment and research experience across both China and Global markets, and has been ranked #1 Commodities Analyst in Asia ex-Japan and #1 in China Energy by Institutional Investor, as well as #1 Analyst in Materials, Energy, and Transportation for A-shares/Hong Kong stocks by Asiamoney.
Our shared vision is to deliver independent analytical perspectives to the market with greater speed and freedom, offering research that stands apart from the output of large institutions that is often distorted by various institutional considerations.

Solemn statement: The above content is based on public information, only represents personal or guests' views. It does not represent any position of AceCamp, any companies, any institutions. The volatility of the stock market is related to many factors. Investment decisions are made by individuals based on their own research and analysis. The purpose of this article or event is the sharing of facts and views and does not constitute any investment suggestions. This article or event content must not be forwarded, reproduced, duplicated, published, modified, or quoted in whole or in part by any institution or individual in any form without the permission of AceCamp and the author. The above content is exclusive to paying clients, and all institutions and individuals are strictly bound by confidentiality obligations and intellectual property agreements. AceCamp is not responsible for the impact of any third party's unauthorized acts while maintaining the rights for legal actions.

Related Recommendations

[NVIDIA's Rack-Level Supremacy vs. AMD's Composability Deficit — Insights from InferenceX v2 Benchmarks

1. This report, grounded in InferenceX v2 benchmarks, systematically compares NVIDIA and AMD across the full-stack frontier LLM inference landscape.
2. NVIDIA's NVL72 rack-level NVLink interconnect and self-reinforcing software ecosystem deliver absolute dominance.
3. AMD's MI355X, while strong in single-node FP8 scenarios, suffers catastrophic performance collapse when composing FP4, disaggregated prefill, and Wide-EP — rooted in software stack deficiencies and compounded by MI455X roadmap delays into Q2 2027.
4. The report also evaluates Blackwell's compute economics and derivative infrastructure investment opportunities.

2026/02/25 23:21Insight](/article/detail/70559209)[The Largest Chip Deal in History — An Analysis of AMD's "Equity-for-Chips" Strategy

This report analyzes AMD's combined 12GW "equity-for-chips" GPU supply agreements with Meta and OpenAI, examining the deal structure, performance-based warrant mechanics, dilution scenarios, and financial impact. It benchmarks AMD's valuation against Nvidia and Broadcom, and assesses execution risks, software ecosystem challenges, and competitive dynamics as AMD pursues a path toward AI compute duopoly status.

2026/03/02 02:56Insight](/article/detail/70559365)[The Logic Behind Hyperscalers' Massive CapEx: Seizing Control of the Compute Lifeline

1. The strategic logic and drivers behind hyperscalers' massive CapEx.
2. The qualitative shift of compute from an R&D tool to core production infrastructure.
3. How hyperscalers seize control of the compute lifeline through warrant-based deals and securing nuclear power.

2026/03/03 23:34Insight](/article/detail/70559434)[The CapEx Black Hole and AI Overcapacity — A $700 Billion Prisoner's Dilemma

1. Breakdown of 2026 Hyperscaler AI Capex approaching $700 billion across five major players;
2. GPU utilization shortfalls, redundant foundation model training, and data center design mismatches;
3. The AI revenue gap, depreciation accounting practices, and funding sustainability concerns;
4. Prisoner's dilemma dynamics shaping the CapEx supercycle outlook.

2026/03/06 01:45Insight](/article/detail/70559500)

[Will agents cause CPU shortages? Can advanced process capacity meet the CPU demands of AI servers? How to solve agent orchestration latency? Focus: TSMC/Nvidia

For a typical inference server, the bottleneck is mostly the HBM bandwidth; however, in the agent era, this may change, with the CPU potentially becoming the new bottleneck limiting computing power. AMD's Lisa Su publicly stated that enterprise customer demand for CPUs is "exceeding expectations," and AI workloads are driving server CPU demand.
This article primarily analyzes: the potential causes of shortages, a comparison of different CPU types (server vs. PC CPU), and whether the current number of TSMC wafers can meet the needs of leading AI server vendors based on current AI server shipments. It also explores how mainstream AI vendors address agent orchestration latency.

2026/03/12 17:28Insight](/article/detail/70559755)[ASX Channel Check: 2026 Advanced Packaging Order Demand and Capacity Expansion Plans, FoCoS Expected to Achieve Mass Production in Q3, Test Business Growth Outlook and Additional Equipment Demand – Focus on TSMC/NVIDIA/AMD/Broadcom/Amkor/Advantest/Teradyne

- Sustained growth momentum in advanced packaging business: Advanced packaging revenue in 2026 is expected to double YoY, with the majority of revenue contribution anticipated from the oS (On-Substrate) segment.
- Capital expenditure highly focused on AI capacity: Over 90% of the company's 2026 CAPEX will be allocated to advanced packaging. oS capacity is expected to achieve a significant 40% increase this year to meet robust demand overflow from TSMC.
- FoCoS progress: AMD is the main customer for FoCoS (Fan-out on Substrate) technology, with mass production expected in Q3 2026, covering the full process from Bump to CoWoS bridge.

2026/03/17 07:24Note](/article/detail/70559882)[2026 GTC Conference Summary: Summary of changes in the industry/hardware/software/total volume; Analysis of matters not mentioned at the conference.

The 2026 GTC conference has just concluded (the original text can be found online). Jensen Huang's remarks at the conference included both aspects that exceeded market expectations and those that raised concerns.
This article mainly analyzes the key changes and market expectations from the GTC-2026 conference across four dimensions (industry changes, hardware changes, software changes, and overall market changes); and also analyzes aspects of the conference that were not fully revealed.

2026/03/17 02:46Insight](/article/detail/70559867)[Channel Check on Leading Chipmakers: MI Series GPU Iteration and Delivery Pace, Foundry Capacity and Yield Bottlenecks, CPU Supply-Demand and Pricing Trends—Focus on Taiwan Semiconductor, Apple, NVIDIA, Intel, etc.

1. MI series GPU iteration and delivery schedule;
2. Foundry capacity and yield bottlenecks;
3. CPU supply-demand and pricing trends.

2026/02/27 07:17Note](/article/detail/70559299)

[Storage Channel Check: Comparison of SRAM/HBM Performance and Application Scenarios, LPU Development Trends and Stacking/Packaging Solutions, HBM4 Progress and Its Impact on SSD/DDR—Focus on NVIDIA/Groq/AMD, etc.

1. Comparison of SRAM/HBM performance and application scenarios;
2. LPU development trends and stacking/packaging solutions;
3. HBM4 progress and its impact on SSD/DDR.

2026/03/09 09:34Note](/article/detail/70559606)[TSMC Channel Check: CPO R&D Progress and Mass Production Challenges, PIC Capacity Status and Expansion Pace, Industry Chain Division of Labor, and Competitive Outlook with Traditional Optical Modules - Focus on NVIDIA/Broadcom/Google/Advantest/USI/Foxconn/Accelink

- Progress and bottlenecks of TSMC's CPO technology;
- ASX's role and business layout in the CPO industry chain;
- Push and attitudes of key clients (NVIDIA, Broadcom);
- Competitive outlook between CPO and traditional solutions.

2026/03/17 08:21Note](/article/detail/70559889)[MLCC March Update—Price Trends, Utilization Rates, and Cost Structure

The following insights are provided by industry experts:
1. The MLCC market has recently experienced price increases. In mid to late November 2025, MLCC production in the Philippines, Malaysia, and Thailand was impacted by typhoons. This led to a 10-15% price increase for high-capacitance MLCCs and a 10% increase for miniaturized products such as 01,005 from late November to December 2025.
2. Price hikes for non-high-capacitance products are mainly driven by rising raw material costs. For example, prices of palladium and copper have doubled, and nickel prices have risen by at least 15% since the beginning of 2026. Manufacturers pricing materials such as nickel paste and nickel powder adjust based on futures market prices, and cost pressures are ultimately passed on to MLCC products.
3. This round of price increases is similar to the situation in 2016-2017, both characterized by temporary shortages. The previous round was mainly driven by surging demand due to the proliferation of 4G communication networks and increased penetration of electric vehicles, resulting in shortages of high-end products and leading major manufacturers to release mid- and low-end orders.

2026/03/06 07:24Note](/article/detail/70559530)[LPU Channel Check: 3D SRAM Capacity Expected to Reach GB Level, Vertical Stacking via Hybrid Bonding, Power and Thermal Feasibility Analysis, Custom HBM Requirements under Feymann's New Architecture

- Regarding the implementation of Feymann's integrated LPU, SRAM cells will be vertically stacked on the logic die. Previously, relevant diagrams have shown the LPU die and SRAM cells stacked in multiple vertical layers above the logic die. Will Hybrid Bonding technology be used for the connection between LPU and GPU?
- Is the overall planned 3D SRAM capacity expected to reach the GB level?
- Under this new architecture, how has the role of HBM changed? Is there a possibility for 3D SRAM to replace HBM, or will it serve as a supplement?
- From a semiconductor process perspective, will integrating SRAM on the GPU pose thermal challenges? Will GPU thermal management be affected?
- Regarding hierarchical storage, with SRAM, HBM, DRAM, and SSD, hierarchical storage requires data prefetching. How is seamless data prefetching across these tiers achieved? In the next-generation architecture, does the HBM base die need to integrate logic for computation or processing to enable prefetching?

2026/03/06 04:40Note](/article/detail/70559526)

[Channel Check on Major Server Manufacturers: Feynman/LPU/CPX Technologies and Cabinet Form Factor Speculation, Switching Network Design Trends and Mass Production Timeline Expectations, Possibility of NVIDIA Adopting OCS

1. Feynman/LPU/CPX technologies and cabinet form factor speculation;
2. Switching network design trends and mass production timeline expectations;
3. Possibility of NVIDIA adopting OCS.

2026/03/19 06:03Note](/article/detail/70559958)[NVIDIA Feymann Channel Check: Analysis of LPU Technology Integration, Key Lies in CUDA Software Stack and Underlying Library Implementation, CPO Addresses NVLink Speed Limitations in Scale-up Scenarios

- Regarding NVIDIA's overall technology roadmap and LPU-related issues. There are currently many rumors that a new chip optimized specifically for inference may be launched at the press conference. Some speculate this could be an LPU chip, while others believe LPU will be integrated into the next-generation Feymann architecture. What is the expert's understanding of NVIDIA's overall roadmap?
- LPU relies heavily on pre-programming and deterministic static processes. How can it be better integrated with CUDA? Since CUDA itself is highly flexible and GPUs are dynamically scheduled, how can these two be effectively integrated?
- This integration with CUDA aims to retain CUDA's flexibility while leveraging Groq's strengths to extend CUDA. Does this require rewriting or extending the underlying operators in the CUDA library? How difficult is this to implement?
- In the Feymann generation, memory bandwidth can be significantly improved through LPU technology integration. Under the new architecture, what are the plans for network structure and NVLink?

2026/03/06 03:07Note](/article/detail/70559520)[CPO/NPO Channel Check: Technology Positioning and Application Scenarios, NPO Shipment Outlook and Impact on Pluggable Optical Modules, CPO Market Penetration Forecast, Component Value Breakdown and Opportunities for Optical Module Vendors – Focus on NVIDIA, Taiwan Semiconductor, Marvell, Broadcom, Suzhou TFC Optical Communication

- How will the development of CPO technology, especially NVIDIA's active promotion, affect overall demand for optical modules? What opportunities exist for optical module vendors in the CPO field?
- What are the specifics regarding NPO shipment plans, main application scenarios, leading vendors, and whether NPO represents an incremental market for optical module vendors?
- How different are NPO production lines from traditional optical module lines? Is conversion possible? If not fully convertible, where do the main differences lie?
- What are the main components of NPO? What is the business scope and value composition for optical module vendors?
- What are the technical specifications and value of external light sources and fiber array units in NPO systems?
- Does Suzhou TFC Optical Communication have the capability to provide a complete solution in the NPO field? What is its role and competitive advantage in NVIDIA's supply chain?
- While advancing CPO, is NVIDIA also deploying other transitional solutions? What is its attitude toward the future application of CPO technology?
- Under the CPO (Co-Packaged Optics) architecture, which segments do traditional optical module vendors mainly participate in? Is there potential to expand business scope through M&A?
- What is the expected future market penetration of CPO technology? Will pluggable optical modules be completely replaced?
- NVIDIA expects to adopt all-optical interconnects within the rack in its future architecture—will this significantly drive CPO penetration at the scale-out level?
- At the scale-up level, what is the technological evolution path and timeline from NPO to CPO?

2026/03/05 02:50Note](/article/detail/70559475)[NVIDIA PCB Supply Chain Transformation: Accelerated Adoption of Ceramic Substrates and Quartz Cloth

NVIDIA's Rubin platform plans to introduce ceramic/glass substrates, aiming to achieve a 4.5-inch large package area through PCB substrate integration and address bottlenecks in heat dissipation and flatness. 2026 will mark the inaugural year for high-end applications of quartz glass cloth, and this solution, with a more mature supply chain than PTFE, is expected to achieve small-batch production in the second half of the year. Severe shortages in upstream T-Glass glass cloth capacity have become the core constraint, with expansion cycles as long as two years, limiting large-scale adoption of new processes in 2027; meanwhile, ABF substrate prices have already risen significantly by about 50% in 2026 due to cost pressures. The unit price of 1.6T optical module PCBs has reached RMB 85,000–90,000 per square meter, requiring M9-grade quartz glass cloth and mSAP processes. The IC substrate industry has entered a high prosperity cycle, with leading manufacturers' utilization rates approaching 90% in 2026Q1.

2026/03/18 06:44Note](/article/detail/70559920)

- 1
- 2
- 3
- 4

Comments

Published

![No Data](https://static.acecamptech.com/system/empty.svg)

No Data

Publisher

[![](https://image.acecamptech.com/avatar/50523361/0.16602141984665542.jpg?x-oss-process=style/avatar)](/organizer/20509829)

[笃研究 ResearchD](/organizer/20509829)

Published 234 Articles

Follow

Latest update

[More>](/organizer/20509829)

- [The Iran War: Not Worth Fighting, Too Costly to Quit

  2026/03/22 01:39](/article/detail/70560046)
- [Cracks in the Fifty-Year Pact: Has the Hormuz Crisis Shaken the Petrodollar Foundation?

  2026/03/21 08:07](/article/detail/70559993)
- [Agentic AI's Compute Explosion Is Real—But Value Only Belongs to Those Who Define the Architecture [GTC/OFC 2026 Series]

  2026/03/21 00:26](/article/detail/70560022)

![img](https://static.acecamptech.com/system/posters/en_article_poster.png)

Related Radars

[Hot Radars >](/radars)

- [总结最近1个月专家对存储行业的观点，争议和共识，投资机会和风险

  已关注雷达](/radars?monitor_id=c59d4783-4c4e-5c92-b477-95b44c579834)
- 存储(包括NAND、SSD、DRAM、HBM、HHD等)的市场格局、价格趋势与产能分布

  +My Radars
- 阿里云 AI 算力基础设施

  +My Radars
- Unity未来的股价Driver是什么

  +My Radars

Recent Event

Change

- [![](https://image.acecamptech.com/generates/20260322/ad83fc442381.png)

  Update on Overseas Market Demand Growth for Balcony Solar-plus-Storage Systems

  Active2026/03/24 Tues 11:00](/eventDetail/60533049)
- [![](https://image.acecamptech.com/generates/20260321/42463f8f6583.png)

  Chinese Mainland Power Semiconductor Channel Check: Rectifier/Diode/MOS Supply-Demand and Cost Dynamics, Outlook on Price Hike Potential, Price Transmission Path, and Bottoming Out of SiC and IGBT Prices

  Active2026/03/25 Wed 11:00](/eventDetail/60533045)
- [![](https://image.acecamptech.com/generates/20260320/37f96fd7087f.png)

  Interpretation of Humanoid Robot Motion Capture Equipment

  Active2026/04/07 Tues 12:00](/eventDetail/60533039)
- [![](https://image.acecamptech.com/generates/20260320/d1287c92dbae.png)

  Power Supply Channel Check: Progress in Three-Side Power and Vertical Power Supply, Evolution of PSU/Power Shelf/HVDC Architectures, and Supply Chain Changes Including Megmeet

  Active2026/03/24 Tues 11:00](/eventDetail/60533029)
- [![](https://image.acecamptech.com/generates/20260320/94b0e654894d.png)

  [Company NDR] SenseTime (0020 HK) Post-FY25 Earnings Management Call

  Active2026/03/30 Mon 07:00](/eventDetail/60533024)

For You

- [Channel Check on Liquid Metal and TIM Materials: Transition from GB300 Gallium-Based to Rubin Indium-Based, TIM1/TIM2 Hierarchy Definition, Per-Card Value and Incremental Estimates for Cold Plate Supporting Materials, Customer Adoption, Market Share Landscape, and New Material Roadmap – Focus on NVIDIA/Foxconn/Boyd/Indium Corporation/Fironda/Sinopec

  Note2026/03/21 12:25](/article/detail/70560044)
- [Comparative Analysis of Major US Energy Storage Companies—Tesla/FLNC/Sungrow

  Insight2026/03/21 02:00](/article/detail/70560037)
- [Agentic AI's Compute Explosion Is Real—But Value Only Belongs to Those Who Define the Architecture [GTC/OFC 2026 Series]

  Insight2026/03/21 00:26](/article/detail/70560022)
- [Google TPU Power Supply Channel Check: V7 5.5kW Sample Validation, Upgrade from 5.5kW to 8.5kW, Comparison of Navitas/Infineon Solutions, Delta as Primary Supplier and Share Allocation for Secondary/Tertiary Suppliers, 2026 Market Size Estimate – Focus on Delta, Lite-On, Quanta, Navitas Semiconductor, Infineon, Google, NVIDIA

  Note2026/03/20 10:26](/article/detail/70560025)
- [Update on Leading Forestry Carbon Sink Companies—Business Model, Project Development, and Cooperation Status

  Note2026/03/20 07:26](/article/detail/70560009)

- 1
- 2
- 3
- 4

What’s Hot

Change

- [Estimates of 2026 Shipments and Product Mix for Ascend, Cambricon, Hygon, etc.; Considerations by ByteDance, Alibaba, etc. for Self-Developed Chips, Ascend, and Overseas Accelerators in Inference Scenarios; Specific Applications of Supernode Products

  Note2026/03/22 04:16](/article/detail/70559897)
- [Pfizer Series Report I: Rapid Advancement of PD-1/VEGF Bispecific Pipeline—Combining Speed, Breadth, and Differentiation

  Insight2026/03/22 04:33](/article/detail/70560048)
- [The Iran War: Not Worth Fighting, Too Costly to Quit

  Insight2026/03/22 01:39](/article/detail/70560046)
- [Lithium Carbonate Price Outlook for 2026Q2—Impact of Zimbabwe and Progress of Mica Mine Resumption

  Note2026/03/22 01:35](/article/detail/70560047)
- [Qifu Technology (QFIN): Under Tight Fintech Regulation, Rapid Loan Rate Compression Leads to Sharply Lower Profit Expectations—When Will the Stock Price Inflection Point Arrive?

  Insight2026/03/21 14:32](/article/detail/70559991)

![logo](https://static.acecamptech.com/system/app/app_logo.svg)APP Download

Android & iOS

![wxchat-official](https://static.acecamptech.com/www/static/png/wxchat-official-DRqP0C4T.png)

![logo](data:image/svg+xml,%3csvg%20width='20'%20height='20'%20viewBox='0%200%2020%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20width='20'%20height='20'%20rx='4'%20fill='%2304CD65'/%3e%3cpath%20d='M12.8315%207.93333C13.015%207.93333%2013.1967%207.94677%2013.3768%207.96677C12.8868%205.69093%2010.4474%204%207.66297%204C4.55%204%202%206.11644%202%208.80395C2%2010.3552%202.84837%2011.6291%204.26605%2012.6172L3.69965%2014.3164L5.67932%2013.3262C6.38769%2013.4661%206.95603%2013.6098%207.66296%2013.6098C7.84066%2013.6098%208.01687%2013.6011%208.19161%2013.5874C8.08097%2013.2097%208.01687%2012.8142%208.01687%2012.4038C8.01688%209.93603%2010.1415%207.93333%2012.8315%207.93333ZM9.78657%206.40184C10.213%206.40184%2010.4954%206.68164%2010.4954%207.1067C10.4954%207.53005%2010.213%207.81375%209.78657%207.81375C9.36213%207.81375%208.93624%207.53005%208.93624%207.1067C8.93624%206.68162%209.36213%206.40184%209.78657%206.40184ZM5.82327%207.81373C5.39888%207.81373%204.97052%207.53003%204.97052%207.10667C4.97052%206.68162%205.39886%206.40182%205.82327%206.40182C6.24769%206.40182%206.53018%206.68162%206.53018%207.10667C6.53018%207.53003%206.24769%207.81373%205.82327%207.81373ZM18%2012.3359C18%2010.0776%2015.7344%208.23682%2013.1898%208.23682C10.4954%208.23682%208.3733%2010.0776%208.3733%2012.3359C8.3733%2014.5981%2010.4954%2016.435%2013.1898%2016.435C13.7538%2016.435%2014.3226%2016.2932%2014.889%2016.1516L16.4423%2017L16.0164%2015.5884C17.1531%2014.7378%2018%2013.6098%2018%2012.3359ZM11.6282%2011.6291C11.3462%2011.6291%2011.0618%2011.3493%2011.0618%2011.0639C11.0618%2010.7825%2011.3462%2010.499%2011.6282%2010.499C12.0565%2010.499%2012.337%2010.7825%2012.337%2011.0639C12.337%2011.3493%2012.0565%2011.6291%2011.6282%2011.6291ZM14.7431%2011.6291C14.4631%2011.6291%2014.1806%2011.3493%2014.1806%2011.0639C14.1806%2010.7825%2014.4631%2010.499%2014.7431%2010.499C15.1675%2010.499%2015.4519%2010.7825%2015.4519%2011.0639C15.4519%2011.3493%2015.1676%2011.6291%2014.7431%2011.6291Z'%20fill='white'/%3e%3c/svg%3e)WeChat Official Account

AceCampTech

Corporate Address

Beijing:307 S3-M26, 3/F, Hopson Place Office Tower, No.A22 Xidawang Road, Chaoyang District, Beijing, China

Hong Kong:66/F, The Center, 99 Queen’s Road Central, Hong Kong

TEL

+86 10 53322308

+852 69069737

Email

[support@acecamptech.com](mailto:support@acecamptech.com)

Copyright©2026 AceCampTech.com. All Rights Reserved.

[Terms of Service](https://terms.acecamptech.com/agreement/index.html)[Privacy Agreement](https://terms.acecamptech.com/privacy/20240120/index.html)

[京ICP备2025158098号-1](https://beian.miit.gov.cn/#/Integrated/index)[京公网安备 11010502043336号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502043336)
