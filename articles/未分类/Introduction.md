---
title: "Introduction"
source: "https://www.acecamptech.com/article/detail/70560045"
category: "未分类"
date: "2026/03/20 15:07"
downloaded: "2026-03-22 20:18:16 JST"
---

# Introduction

In-Depth Analysis of Satellite Power Systems: A Panoramic View of a 100-Billion Market and Core Technologies

Chinese

EN

The original version is in Chinese FYI

In-Depth Analysis of Satellite Power Systems: A Panoramic View of a 100-Billion Market and Core Technologies

VIPOriginalIndustry：TMT, Semiconductor, ​Manufacturing

2026/03/21 14:42:01

Views 3590

Likes 0

Quick-Q

Summary

1. Strategic importance elevated, value contribution highlighted: Satellite power systems have evolved from auxiliary supporting equipment to critical subsystems that determine satellite platform performance, lifespan, and commercial success. Their value accounts for as much as 20%-30% of total satellite manufacturing costs, making them a core segment in the industry value chain.
2. Clear technology drivers, efficiency and lightweight as the main theme: Industry technology evolution centers on four directions—multi-junction GaAs cells, flexible roll-out solar arrays, intelligent MPPT controllers, and high energy density storage. The core objective is to achieve high efficiency, lightweight, and long lifespan, meeting the mass production and cost reduction needs of mega-constellations.
3. Vast market potential, 10-year certainty reaching 100 billion RMB: Driven by commercial space, especially the construction of global LEO communication constellations, the global satellite power system market is expected to reach RMB 100-180 billion between 2026 and 2035. Solar arrays, as the value core, will account for RMB 70-126 billion, with high certainty and growth flexibility.
4. Bipolar competitive landscape, integration evolution breeds opportunities: The industry presents a dual structure of "state-owned teams leading high-reliability missions, commercial companies focusing on scale markets." In the future, enterprises with full-stack technical capabilities, large-scale delivery capacity, and cost control advantages will secure leading positions amid industry chain integration and market expansion.

The full text is 6675 words, estimated reading time 14 minutes

VIP Free

# **Introduction**

As the space industry transitions from "national projects" to the "commercial era," the race to build LEO satellite internet constellations has become the core battleground for global technology and capital. Tens of thousands of satellites will be launched into low Earth orbit to form a global space-based communication network. This is not only a revolution in communication technology but will also give rise to an entirely new space economy ecosystem. However, amid this journey to the stars and the sea, a simple yet crucial question underpins all grand visions: How can these satellites be supplied with continuous, stable, and reliable energy in the remote, harsh, and physically unserviceable environment of space? The satellite power subsystem is the key to this question. It is no longer an inconspicuous "supporting role" on spacecraft, but the "energy heart" that directly determines the functional ceiling, on-orbit lifespan, and commercial returns of the satellite platform. Currently, driven by the strong demand for large-scale, low-cost, and rapid-iteration commercial space, satellite power technology is undergoing a comprehensive transformation from materials and devices to system architecture, and the industry chain faces a historic opportunity for value revaluation and structural reshaping. This report aims to systematically outline the underlying logic of the industry, deeply analyze its technological core, quantitatively assess market potential, and interpret the evolution trends of the competitive landscape.

# **Key Insights**

1. **Strategic importance elevated, value contribution highlighted**: Satellite power systems have evolved from auxiliary supporting equipment to critical subsystems that determine satellite platform performance, lifespan, and commercial success. Their value accounts for as much as 20%-30% of total satellite manufacturing costs, making them a core segment in the industry value chain.

2. **Clear technology drivers, efficiency and lightweight as the main theme**: Industry technology evolution centers on four directions—multi-junction GaAs cells, flexible roll-out solar arrays, intelligent MPPT controllers, and high energy density storage. The core objective is to achieve high efficiency, lightweight, and long lifespan, meeting the mass production and cost reduction needs of mega-constellations.
3. **Vast market potential, 10-year certainty reaching 100 billion RMB**: Driven by commercial space, especially the construction of global LEO communication constellations, the global satellite power system market is expected to reach RMB 100-180 billion between 2026 and 2035. Solar arrays, as the value core, will account for RMB 70-126 billion, with high certainty and growth flexibility.
4. **Bipolar competitive landscape, integration evolution breeds opportunities**: The industry presents a dual structure of "state-owned teams leading high-reliability missions, commercial companies focusing on scale markets." In the future, enterprises with full-stack technical capabilities, large-scale delivery capacity, and cost control advantages will secure leading positions amid industry chain integration and market expansion.

# **01 Satellite Power System: The "Energy Heart" Accounting for 20%-30% of Satellite Value**

The satellite power system is the only on-orbit energy supply and management system for spacecraft, responsible for the entire chain from solar energy capture, power storage, and power regulation to precise distribution. Its performance and reliability are absolute prerequisites for satellite survival and mission execution; once it fails, satellites worth hundreds of millions instantly become space debris.

A complete satellite power system is a highly complex electromechanical-thermal integrated system, precisely coordinated by **six major units**: **solar array, battery pack, power controller, array drive mechanism, array deployment mechanism, and sun sensor**. These six components have clear divisions of labor, forming an autonomous energy loop of "generation-storage-management-optimization," ensuring that satellites can provide uninterrupted, stable power to the platform and various payloads "24/7" as they periodically experience harsh orbital environments of sunlight and Earth's shadow.

In the cost structure of satellite manufacturing, the power subsystem holds a pivotal position. **The total value of the satellite power system accounts for about 20%-30% of the total satellite manufacturing cost**. This significant proportion means that for a high-orbit satellite with a manufacturing cost of RMB 100 million, the power system alone is worth RMB 20-30 million. The high value share stems from its extreme technical complexity, stringent reliability requirements, and the high cost of special materials and processes. Within the power system, value is also highly concentrated. **Solar arrays, as the core of power generation, account for 60%-80% of the entire power system cost**. This is because solar wings not only incorporate high-barrier, high-efficiency solar cells (such as multi-junction GaAs), but also integrate complex lightweight composite structures and highly reliable deployment and drive mechanisms, representing the convergence of material science, mechanical engineering, and power electronics. This value structure clearly indicates that the satellite power industry, especially the solar array segment, is a typical "high-technology-barrier, high-value-added" advanced manufacturing field.

# **02 Overview of the Six Major Units of Satellite Power Systems**

Figure: Composition of Satellite Power System

![](https://image.acecamptech.com/articles/70560045/e6f5a401-0cba-41f2-afec-9dd74f809131.png)

Data source: **"Design and On-Orbit Test of a Modular Power System for CubeSat"**

The six core units of the satellite power system together form a sophisticated life-support system capable of autonomously adapting to the space environment and intelligently managing energy flow:

Table: Six Core Units of Satellite Power System

![](https://image.acecamptech.com/articles/70560045/c48af7ad-7896-4c35-b7a7-c7cf3eea5782.png)

Data source: **"Design and On-Orbit Test of a Modular Power System for CubeSat," compiled by the author**

These six units are tightly coupled through cable networks, data buses, mechanical interfaces, and thermal control systems, forming an autonomous energy loop in orbit. Among them, **solar array, battery pack, and power controller** are the "three cores" determining basic system performance, while the drive, deployment mechanisms, and sensors are "key enablers" for efficient and reliable power generation.

# **03 In-Depth Analysis of Core Units in Satellite Power Systems**

This section provides an in-depth analysis of the three core units with the highest value and technological concentration—battery pack, solar array, and power controller.

## **Battery Pack**

- **Function**: As the satellite's only energy storage unit, its core function is to provide continuous and stable power output for the entire satellite when energy input is interrupted (eclipse period) or when load power demand surges, serving as the "ballast" ensuring mission continuity.
- **Principle**: The space sector has fully transitioned from early nickel-cadmium and nickel-hydrogen batteries to **lithium-ion batteries**. Their working principle relies on the reversible intercalation and deintercalation of lithium ions between the anode and cathode materials. During charging, external energy forces lithium ions to leave the cathode (such as lithium cobalt oxide, lithium iron phosphate), pass through the electrolyte, and intercalate into the graphite anode; during discharge, the process reverses, and lithium ions return to the cathode, generating current. Aerospace battery packs consist of dozens to hundreds of individual cells precisely connected in series and parallel, equipped with complex battery management systems for voltage balancing, thermal management, and state diagnostics.
- **Development Trends**: **Higher energy density**: By applying new materials such as silicon-carbon anodes and high-nickel cathodes, the energy density of individual cells is increased, providing more energy for the same weight and volume, directly extending satellite lifespan or supporting larger payloads. **Longer cycle life and higher safety**: The development of solid-state electrolytes and optimized electrode interfaces aims to fundamentally solve the thermal runaway risk of liquid electrolyte batteries and achieve ultra-long cycle life of over 10,000 cycles, meeting the 8-10 years or longer on-orbit lifespan required by LEO constellation satellites. **Exploration of new storage technologies**: **Lithium-ion capacitors** are an important direction, seeking to combine the high energy density of lithium-ion batteries with the high power and long cycle characteristics of supercapacitors, potentially addressing instantaneous high-power loads and improving system response speed and reliability.
- **Technical Bottlenecks**: **Space environment adaptability**: The vacuum, extreme temperatures (ranging from -100°C to over +100°C), and high-energy particle radiation in space pose extreme challenges to battery materials, sealing processes, and thermal management design. Degradation of charge/discharge performance at low temperatures and lifespan and safety issues at high temperatures are particularly pronounced. **Consistency management and long lifespan**: Battery packs are made up of many cells in series and parallel; any single cell's degradation or failure can trigger a chain reaction. Ensuring high consistency among hundreds of cells over more than a decade in orbit is a major challenge for BMS design and cell screening processes. **Limitations of ground verification**: Ground tests cannot fully simulate the long-term combined effects of the space environment, and the actual degradation mechanisms and lifespan prediction of batteries in orbit are uncertain, requiring significant design margins for reliability, which increases costs.

**Figure: Satellite Power System Battery Pack**

![](https://image.acecamptech.com/articles/70560045/c4eb1dfa-7d73-48c7-8c86-5973145a7312.png)

Data source: **"Design and On-Orbit Test of a Modular Power System for CubeSat"**

## **Solar Array**

- **Function**: The primary power generation device during satellite operation, responsible for converting inexhaustible solar energy into usable electrical energy for the satellite. Its output power and stability are the energy foundation for all satellite functions.
- **Principle**: Based on the photovoltaic effect. When photon energy exceeds the bandgap of the semiconductor material (solar cell), electron-hole pairs are generated, which are separated by the built-in electric field to form photovoltage and photocurrent. The mainstream technology is **triple-junction GaAs cells**, which stack three sub-cells, each absorbing different bands of the solar spectrum, with theoretical conversion efficiency far surpassing traditional silicon cells.
- **Development Trends**: **Higher cell efficiency**: Evolving from triple-junction GaAs to **quadruple-, quintuple-, and even sextuple-junction GaAs cells**, with more refined band engineering to capture a broader solar spectrum, pushing lab conversion efficiency to 40% or higher. **Thin-film flexible solar cells** (such as CIGS) are also used in certain lightweight satellites. **Flexible and lightweight configurations**: Evolving from traditional **rigid solar wings** (heavy, low stowage ratio) to **semi-rigid solar wings**, and further to **flexible solar wings** (especially roll-out flexible solar wings). ROSA enables extremely high power-to-weight ratios and minimal launch envelope volume, serving as a key technology for cost reduction and efficiency improvement in mega-constellations like Starlink. **High voltage and high power**: As satellite power demand grows to tens of kilowatts, the operating voltage of solar arrays is increasing from the traditional 100V class to 300V or higher to reduce transmission losses, but this introduces new space environment effects such as electrostatic discharge and plasma arcs.
- **Technical Bottlenecks**: **Material and epitaxy process barriers**: The metal-organic chemical vapor deposition epitaxy process for multi-junction GaAs cells is extremely complex, requiring atomic-scale control of hundreds of material layers. Equipment is expensive, yield control is difficult, and only a handful of companies worldwide can achieve stable mass production, resulting in high costs. **Engineering challenges of flexible solar wings**: Flexible substrate materials must combine ultra-thinness, high strength, weather resistance, radiation resistance, and dimensional stability—often conflicting properties. The deployment mechanism's dynamic behavior under microgravity and extreme temperature cycles is complex, and reliable deployment and long-term on-orbit shape retention are major challenges. Full physical simulation testing on the ground is difficult and costly. **Space debris protection and reliability**: Large flexible solar wings have a huge surface area, significantly increasing the risk of being punctured by micro-debris. Designing redundant circuits and protective structures to ensure system operation after local damage is a design challenge.

**Figure: Satellite Power System Solar Array**

![](https://image.acecamptech.com/articles/70560045/35f15751-a9d3-46b7-a9de-1690f2b040d9.png)

Data source: **"Design and On-Orbit Test of a Modular Power System for CubeSat"**

## **Power Controller**

- **Function**: As the command center of the power system, it coordinates power generation, storage, and consumption, maintains bus voltage stability, protects electrical devices, and optimizes energy allocation and usage.
- **Principle**: The core is a power electronics conversion and control system. There are two main technical routes: **S3R**: A **direct energy transfer** topology. It uses sequential shunt regulators to dissipate excess energy from the solar array as heat. It is simple and reliable, the mainstream choice for many high-reliability satellites, but less efficient. **MPPT**: A **maximum power point tracking** topology. It uses DC-DC converters to dynamically adjust the solar array's operating point for maximum power output, improving energy utilization by 10%-30% over S3R, but with more complex circuitry and slightly greater reliability challenges.
- **Development Trends**: **High efficiency and high power density**: Widespread adoption of third-generation semiconductor devices (such as SiC, GaN) increases switching frequency, reduces passive component size, and enables miniaturization and lightweighting of power controllers to meet high-power satellite needs. **Intelligent and health management**: Integration of advanced algorithms enables load prediction, adaptive energy management, fault diagnosis, and autonomous reconfiguration. Deep interaction with onboard computers allows mission-based energy scheduling, maximizing scientific or commercial output. **Modularization and standardization**: To support mass production of commercial satellites, power controllers are moving toward modular, off-the-shelf products, meeting different satellite needs through combinations of power modules, greatly shortening development cycles and reducing costs.
- **Technical Bottlenecks**: **Contradiction between high reliability and long lifespan**: Space-grade high-reliability components are extremely expensive and have long lead times. Using industrial or automotive-grade components with derating design to achieve long life and high reliability imposes stringent requirements on circuit design, thermal design, and screening/aging processes. **Complex electromagnetic compatibility**: As a major source of switching noise, the power controller can easily interfere with sensitive payloads (such as communication or detection payloads) in the confined satellite cabin. Achieving excellent EMC performance under tight space and weight constraints is a major system integration challenge. **Maturity of MPPT technology in space applications**: Although MPPT offers clear efficiency advantages, its long-term operational stability in complex space plasma environments and adaptability to partial shading of solar arrays still require more on-orbit flight data. Replacing S3R in high-value missions will take time.

**Figure: Satellite Power System Power Controller**

![](https://image.acecamptech.com/articles/70560045/5e037fb8-e1aa-4bfd-99f3-af826aaad4f4.png)

Data source: **"Design and On-Orbit Test of a Modular Power System for CubeSat"**

# **04 A 100-Billion Market Opportunity**

As a high-value subsystem of spacecraft, the market size of satellite power systems is directly correlated with global satellite launch volume. Based on current industry consensus and future space industry development trends, this section provides a quantitative estimate of the market size for 2026-2035.

**Core Estimation Assumptions:**   
1. **Estimation period**: 2026 to 2035, a total of 10 years.

2. **Unit satellite value benchmark**: Assume the average manufacturing cost per satellite is **RMB 20 million**.
3. **Power system value share**: Satellite power systems account for about 20%-30% of total satellite manufacturing cost. For model simplification and a neutral estimate, use a median value of **25%** as the calculation basis. Thus, **average power system value per satellite = RMB 20 million \* 25% = RMB 5 million**.
4. **Solar array value share**: Solar arrays account for 60%-80% of the power system cost. Use a median value of **70%** as the calculation basis. Thus, **average solar array value per satellite = RMB 5 million \* 70% = RMB 3.5 million**.
5. **Launch volume forecast scenarios**: Drawing on forecasts from the International Satellite Association, Euroconsult, and others for LEO constellation deployment, three total satellite launch scenarios are set: **Conservative scenario**: 20,000 satellites launched over ten years, considering global economic fluctuations, constellation plan delays, or underfunding. **Base scenario**: 28,000 satellites launched over ten years, reflecting steady deployment of major global LEO broadband constellations such as Starlink, Kuiper, and China SatNet as planned. **Optimistic scenario**: 36,000 satellites launched over ten years, considering further declines in rocket launch costs, new national constellation plans, and incremental demand from expanded space applications.

**Market Size Estimation Table (2026-2035)**

![0](https://image.acecamptech.com/article_image/50524811/0.43492096265180336.jpeg)

**Data source: Author's own calculations**

**A 100-Billion Certainty Market**: Over the next decade (2026-2035), the global satellite power system market will total **RMB 100-180 billion**. The base scenario market size is **RMB 140 billion**. As the core component, solar arrays will account for **RMB 70-126 billion**, with the base scenario at **RMB 98 billion**. This constitutes a highly certain high-end equipment market.

**Clear growth drivers**: The core market driver is the large-scale deployment of global LEO communication constellations. This demand is highly planned, large in volume, and long in duration, providing upstream power system suppliers with clear order visibility. Stable demand from traditional satellite sectors such as remote sensing, meteorology, and scientific research forms another market cornerstone.

**Broad industry chain extension**: This estimate focuses on the hardware value of power systems in satellite manufacturing. The extended value of the industry chain is also considerable, including upstream special materials (such as GaAs substrates, high-performance composite films), high-end components, midstream testing and verification services, and potential on-orbit energy management and life extension services for satellites. The overall industry ecosystem value far exceeds hardware manufacturing alone.

# **05 Industry Competitive Landscape: Divergence and Synergy Between State-Owned and Commercial Forces**

The satellite power system industry has formed a dual competitive landscape dominated by national research institutes and rapidly rising commercial companies. The two differ in technology paths, market positioning, and customer groups, but also cooperate and complement each other.

## **State-Owned Teams**

State-owned teams mainly refer to large research institutes and their industrialization platforms under China Aerospace Science and Technology Corporation, China Aerospace Science and Industry Corporation, China Electronics Technology Group, etc. They undertake major national space projects, define technical systems and reliability standards, and possess complete R&D systems from materials and devices to system integration. They are responsible for all power system tasks for major national programs such as manned spaceflight, lunar exploration, and BeiDou navigation, with products verified under extremely stringent on-orbit conditions. Their primary goal is to fulfill national missions, with relatively low sensitivity to cost.

**Representative entities**: **Shanghai Institute of Space Power-Sources (SISP, CASC 811)**: The most important domestic space power system integrator, covering all six major units, a typical "state-owned team" representative. **Tianjin Power Research Institute (CETC 18)**: A comprehensive authority in chemical and physical power sources, with deep expertise in space energy storage batteries and solar cells. **Relevant units under China Academy of Space Technology**: As satellite system integrators, their subsidiaries lead in power system design and SADA (solar array drive mechanism).

## **Commercial Companies**

With the rapid development of China's commercial space sector, a group of private enterprises has quickly gained a foothold in the commercial satellite power market through flexible mechanisms, rapid R&D iteration, and extreme cost control, becoming an indispensable force. They focus on commercial space market demand; have agile R&D processes, excel at cost reduction using industrial-grade components and mature supply chains; offer short delivery cycles and fast customer service; and are more innovative in emerging or high cost-performance technology paths such as flexible solar arrays, low-cost SADA, and intelligent power controllers.

**Major commercial companies**: **DianKe Blue Sky**: As a CETC subsidiary, it is both a key state-owned team member and an active commercial market player, with high market coverage and a complete product line. **Suzhou Fuchang Space Technology Co., Ltd.**: The first domestic private company specializing in commercial satellite power systems, offering full-stack solutions from unit to system integration, with outstanding on-orbit performance. **Dehua Chip**: Focused on space solar cells, competitive in upstream core materials such as high-efficiency GaAs epitaxial wafers. **MicroMotion Space**: A well-known SADA (solar array drive mechanism) supplier in China's commercial space sector. **Tianyin Interstellar**: Market leader in attitude measurement components such as star sensors and sun sensors.

## **Evolution Trends in the Competitive Landscape**

Currently, the competitive landscape features both "stratification" and "integration." In high-end, high-reliability mission fields, state-owned teams have an absolute advantage due to deep expertise. In the commercial LEO constellation market, which values cost-effectiveness and rapid iteration, commercial companies have become the main suppliers. In the future, the boundaries between the two may blur further: state-owned teams may participate in commercial competition by establishing market-oriented subsidiaries or incubation platforms, while commercial companies, after accumulating sufficient on-orbit data and technology, may penetrate higher-end markets. Enterprises capable of integrating "high-reliability design" and "low-cost manufacturing," with **in-house development of core units and system integration capabilities**, will occupy more advantageous positions in future competition.

# **Conclusion**

The satellite power system industry stands at a golden development period supported by certain demand, continuous technological innovation, and clear business models. As a key subsystem accounting for 20%-30% of satellite value, its market is deeply tied to the global space industry cycle, especially the progress of LEO satellite internet deployment. The main lines of technological evolution clearly point to four directions: high efficiency (multi-junction GaAs, MPPT), lightweight and high stowage ratio (flexible solar arrays), high energy density and long lifespan (new energy storage technologies), and intelligence (health management).

Estimates based on the unit satellite value model show that the global satellite power system market will be a highly certain track worth **hundreds of billions of RMB** over the next decade, with solar arrays as the value core, accounting for more than half. This provides ample growth space for industry chain enterprises.

On the competitive front, traditional "state-owned teams" and emerging "commercial forces" constitute the two pillars of the industry, playing irreplaceable roles in different market dimensions and promoting and integrating with each other through competition. The core logic for investing in this track is to identify leading enterprises that have built solid technical barriers, possess products verified in orbit, and are deeply bound to mainstream downstream satellite manufacturers or constellation operators. As the construction of global space infrastructure accelerates, the "heart" industry that powers these "stars" will usher in a long-term and vibrant growth era.

## **Risk Disclosure:** The content of this article is for industry analysis only and does not constitute any investment advice.

Follow-up

[With China SatNet's pricing pressure, what is the cost-reduction limit for CETC Blue Sky and Dehua Chip in flexible solar arrays, and is margin compression already priced in?](/chat?title=With%20China%20SatNet's%20pricing%20pressure,%20what%20is%20the%20cost-reduction%20limit%20for%20CETC%20Blue%20Sky%20and%20Dehua%20Chip%20in%20flexible%20solar%20arrays,%20and%20is%20margin%20compression%20already%20priced%20in?) [Given the high barriers of multi-junction GaAs epitaxy, can Dehua Chip's yield support China SatNet's dense launches? Would lower yields trigger an industry-wide valuation downgrade?](/chat?title=Given%20the%20high%20barriers%20of%20multi-junction%20GaAs%20epitaxy,%20can%20Dehua%20Chip's%20yield%20support%20China%20SatNet's%20dense%20launches?%20Would%20lower%20yields%20trigger%20an%20industry-wide%20valuation%20downgrade?)

商业航天卫星互联网卫星SPACEX

Likes

Dislikes

1

Share

[![](https://image.acecamptech.com/avatar/50524811/1734398740530.jpg?x-oss-process=style/avatar)](/organizer/20510256)

[Faby Luo](/organizer/20510256)

Acecamp analyst

Follow

Solemn statement: The above content is based on public information, only represents personal or guests' views. It does not represent any position of AceCamp, any companies, any institutions. The volatility of the stock market is related to many factors. Investment decisions are made by individuals based on their own research and analysis. The purpose of this article or event is the sharing of facts and views and does not constitute any investment suggestions. This article or event content must not be forwarded, reproduced, duplicated, published, modified, or quoted in whole or in part by any institution or individual in any form without the permission of AceCamp and the author. The above content is exclusive to paying clients, and all institutions and individuals are strictly bound by confidentiality obligations and intellectual property agreements. AceCamp is not responsible for the impact of any third party's unauthorized acts while maintaining the rights for legal actions.

Related Recommendations

[Decoding Electric Propulsion for LEO Satellites: Technology, Industry Progress, and the CNY 10 Billion Opportunity

Against the backdrop of a commercial space boom and the global race for LEO satellite constellations, a silent revolution is underway, reshaping the core performance and business models of satellite platforms. The focus of this revolution is not on payloads or communication links, but on the 'heart' and 'legs' of satellites—the propulsion system. For decades, satellites have relied on chemical propulsion for orbit maintenance, attitude control, and deorbiting. However, as mega-constellations comprising tens of thousands or even hundreds of thousands of satellites are planned, the limitations of traditional chemical propulsion in terms of efficiency, cost, weight, and controllability are becoming increasingly apparent. Electric propulsion, represented by Hall thrusters, is rapidly evolving from a 'cutting-edge option' for high-orbit satellites and deep space exploration to the 'economic standard' and 'performance necessity' for large-scale deployment of LEO communication and remote sensing constellations, thanks to its high specific impulse, long lifespan, precise micro-thrust control, and lightweight system design. This report aims to go beyond the technical surface, thoroughly analyze the physical and commercial logic behind electric propulsion replacing chemical propulsion, deconstruct its diverse technological pathways and core challenges, and, based on rigorous quantitative models, map out the market blueprint and industry landscape for this critical growth phase from 2026 to 2035.

2026/03/20 15:07Insight](/article/detail/70560032)[A Trillion-Yuan Blue Ocean: Satellite Laser Communication—Technology, Market Potential, and Global Landscape

1. Generational technological leap is the core logic: Leveraging its ultra-high frequency and extremely narrow beam, laser communication comprehensively surpasses traditional microwave communication in terms of speed, confidentiality, anti-interference, and terminal miniaturization, making it the inevitable choice to address the future deluge of massive space data.
2. Global race, with the US leading but competition intensifying: The US, represented by SpaceX and NASA, has achieved large-scale deployment and cutting-edge validation; Europe is advancing steadily based on mature systems; China has completed multiple key in-orbit experiments and is accelerating its catch-up. The three regions show significant gaps in industrialization and application scale.
3. Cost and reliability are key to industrialization: Despite its prominent advantages, the complexity of high-precision PAT systems, atmospheric transmission interference, and high initial costs (especially for coherent systems) remain major hurdles for large-scale adoption.
4. Dual-driven market by military and civilian demand: Rigid demand for military communications continues to drive high-end technological breakthroughs, while broad civilian scenarios such as global broadband internet constellations (e.g., Starlink), maritime communications, and emergency communications provide fertile ground for explosive commercial growth.
5. Market on the eve of an explosion, industry chain opportunities emerging: As LEO constellation construction enters its peak, the laser communication terminal market is expected to see exponential growth. From core optical components and precision control systems to system integration and operational services, the entire industry chain is brimming with significant opportunities.

2026/03/20 14:29Insight](/article/detail/70560031)[Analysis of Phased Array Antennas: Standard Configuration for Space-Earth and a Trillion-Yuan Value Plateau

Key Points
1. Phased array antennas replace mechanical scanning with electronic control, enabling real-time, precise, and programmable control of electromagnetic wave spatial direction.
2. This technology upgrades antennas from single radiators to system-level core units with multi-beam, multi-function, and anti-jamming capabilities.
3. In terms of technical pathways, active phased arrays, leveraging distributed T/R architecture, have become the mainstream solution for radar and satellite communications.
4. The industry exhibits a dual-engine pattern of "high-value spaceborne + large-scale ground deployment," driving the market toward a trillion-yuan scale.
5. Essentially, phased array antennas are reshaping communication and sensing systems, making "spatial resources" a key capability that can be software-defined and scheduled.

2026/03/19 13:21Insight](/article/detail/70559982)[The Triangular Trade-off of Efficiency, Weight, and Cost: Why Does Musk Use Crystalline Silicon While China Uses Gallium Arsenide?

1. The main logic of technological evolution is "efficiency first": The iteration of satellite power sources from crystalline silicon to gallium arsenide (from single-junction to multi-junction, from rigid to flexible) is fundamentally driven by the pursuit of higher photovoltaic conversion efficiency, aiming to reduce launch weight and extend on-orbit lifespan—core requirements for space missions.
2. The core of decision-making lies in "full lifecycle cost" trade-offs: The choice of technology route is not simply a comparison of cell manufacturing costs, but a complex balance between manufacturing costs and launch/operation costs. The high unit price of high-efficiency cells must be offset and surpassed by the system weight reduction and lifespan extension they bring.
3. The "binary opposition" of application scenarios drives route differentiation: The current market has formed a clear pattern of technology-to-scenario matching. Mega-constellations in low Earth orbit (LEO) that pursue extreme cost-effectiveness and short lifespans (such as Starlink) tend to use mature, low-cost crystalline silicon cells; while high-value, long-lifespan, high-orbit traditional satellites firmly choose high-efficiency, highly reliable gallium arsenide cells. The difference in choices between Musk and the mainstream aerospace sector essentially stems from differences in business models and mission requirements.
4. The future focus of competition will be on "specific power" and "flexibility": The next phase of technological competition will shift from a sole pursuit of "high efficiency" to a focus on higher "power-to-mass ratio" and "power-to-volume ratio." Flexible thin-film gallium arsenide cells epitomize this trend. Despite manufacturing challenges, their revolutionary advantages in weight reduction and stowage have made them a strategic high ground for major space powers such as China and the US.

2026/03/19 12:43Insight](/article/detail/70559979)

[Behind the $2.97 Billion Contract: The U.S. Ramps Up Strategic Satellite Communications, AEHF System Continues to Expand

Recently, the U.S. Department of Defense announced a contract modification for the Advanced Extremely High Frequency (AEHF) satellite communication terminal project, adding $2.01 billion and raising the total contract value from the original $960 million to $2.97 billion, with the project timeline extended to 2031. The contract was issued by the Strategic Communications Directorate of the Air Force Nuclear Weapons Center and is primarily undertaken by RTX Corporation for R&D and production.
On the surface, this appears to be a routine budget adjustment for a defense contract. However, viewed in a broader context, it reflects the U.S.'s long-term logic in building its strategic satellite communication system. The AEHF system is not an ordinary communications satellite project, but a critical component of the U.S. strategic command and control communications network. Its core objective is to maintain stable command and communication capabilities even under highly contested or extreme conditions.
As military communications increasingly evolve toward network-centric, anti-jamming, and high-security standards, the construction of strategic communication systems like AEHF often signals long-term and stable industry demand.

2026/03/16 15:36Insight](/article/detail/70559864)[Expert Exchange with Leading Domestic Probe Manufacturer – Progress in Cooperation with Overseas Clients such as NV, Changes in GB300 and Rubin Probe Demand, Breakthroughs by Domestic Manufacturers

Analysis of the market expansion and logic for Nvidia B300 and Rubin FT probe business.
Progress of the company’s FT and CP business with Nvidia; progress with domestic memory manufacturers.

2026/03/19 03:51Note](/article/detail/70559954)[NVIDIA PCB Supply Chain Transformation: Accelerated Adoption of Ceramic Substrates and Quartz Cloth

NVIDIA's Rubin platform plans to introduce ceramic/glass substrates, aiming to achieve a 4.5-inch large package area through PCB substrate integration and address bottlenecks in heat dissipation and flatness. 2026 will mark the inaugural year for high-end applications of quartz glass cloth, and this solution, with a more mature supply chain than PTFE, is expected to achieve small-batch production in the second half of the year. Severe shortages in upstream T-Glass glass cloth capacity have become the core constraint, with expansion cycles as long as two years, limiting large-scale adoption of new processes in 2027; meanwhile, ABF substrate prices have already risen significantly by about 50% in 2026 due to cost pressures. The unit price of 1.6T optical module PCBs has reached RMB 85,000–90,000 per square meter, requiring M9-grade quartz glass cloth and mSAP processes. The IC substrate industry has entered a high prosperity cycle, with leading manufacturers' utilization rates approaching 90% in 2026Q1.

2026/03/18 06:44Note](/article/detail/70559920)[Domestic CW Light Source Channel Check: Commercialization Pace and High-Power Sample Delivery Chain, MOCVD Equipment Supply/Lead Time/Industry Yield Rate/Bottlenecks, 70/100mW Capacity Structure and Reliability Progress under 800G Demand - Focus on Yuanjie Tech, Changguang Huaxin, HGTech, Zhongji Xuchuang, NVIDIA, NAURA, Eoptolink, Source Photonics

- Focus: Exploring the commercialization path from R&D to small-batch/mass production for CPO and prospects for breakthroughs in high-power CW localization.
- Structure: Deconstructing and evaluating capabilities across "Epitaxy/MOCVD—Back-End Packaging & Thermal Management—Customer Certification/Sample Delivery".
- Pace: Outlook on equipment lead times, production line construction, yield ramp-up, and the progression from 70–100mW reliability validation to high-power iteration.

2026/03/17 19:07Note](/article/detail/70559904)

[3D DRAM Materials & Architecture Primer -- The End and Reconstruction of Traditional Capacitor Systems

1. The physical limits of traditional MIM capacitors have been reached, driven by aspect ratio and quantum tunneling challenges.
2. Three competing 3D DRAM architectures—CUA, STC, and eDRAM—are in a technological race with unresolved engineering challenges.
3. The transition necessitates a structural overhaul of the material and equipment systems, including new electrodes and ALD technologies.

2026/03/17 09:28Insight](/article/detail/70559873)[2026 GTC Conference Summary: Summary of changes in the industry/hardware/software/total volume; Analysis of matters not mentioned at the conference.

The 2026 GTC conference has just concluded (the original text can be found online). Jensen Huang's remarks at the conference included both aspects that exceeded market expectations and those that raised concerns.
This article mainly analyzes the key changes and market expectations from the GTC-2026 conference across four dimensions (industry changes, hardware changes, software changes, and overall market changes); and also analyzes aspects of the conference that were not fully revealed.

2026/03/17 02:46Insight](/article/detail/70559867)[Channel Check on Leading Packaging Companies: CPO Packaging Yield and Capacity Allocation Trends, CoWoS Front-/Back-End Profitability, Google CPO Roadmap—Focus on NVIDIA, Broadcom, AMD, MediaTek, Google, etc.

1. CPO packaging yield and capacity allocation trends;
2. CoWoS front-/back-end profitability;
3. Google CPO roadmap.

2026/03/16 06:42Note](/article/detail/70559829)[The AI Agent Economy: What Circle Truly Wants to Bet On for the Future

If Circle is only seen as a stablecoin company, it is easy to underestimate the real signals the company released in this earnings call. On the surface, Circle discussed USDC growth, on-chain payment expansion, Arc testnet progress, and the gradual clarification of stablecoin regulation. However, at a deeper level, the company is actually presenting an entirely new narrative: stablecoins are not just for crypto trading, cross-border payments, or even asset tokenization—their most imaginative future application may be serving the AI agent economy. From this perspective, Circle is no longer just telling the story of 'stablecoin growth,' but is attempting to define a new question: when machines begin to work, transact, collaborate, and settle, what kind of monetary system will they use?

2026/03/12 13:38Insight](/article/detail/70559748)

[![](https://image.acecamptech.com/generates/20260318/616237545372.png)

Expert Talk on Domestic Probe Leader: Progress with Overseas Clients like NVIDIA, Demand Changes for GB300/Rubin Probes, and Breakthroughs by Domestic Manufacturers

2026/03/18 Wed 11:00 Event](/eventDetail/60532945)[CCL and HBM Drive Surge in High-End Spherical Silica Demand; Chemical Process Domestic Substitution Enters Critical Phase

- CCL and HBM are driving the evolution of spherical silica toward submicron/nanometer grades, with M9 CCLs seeing filler ratios rise to 40% and absolute per-board usage increasing with grade advancement.
- Diverging process routes: Flame fusion dominates micron grades; VMC (combustion) method produces 0.6–1.0μm products for HBM and below M8; Sol-gel chemical synthesis yields sub-0.5μm high-end products for M9.
- Significant room for domestic substitution: Domestic submicron chemical-process products are priced at RMB 300,000–600,000/ton, while Japanese imports are double; the core gap lies in purity and particle uniformity.

2026/03/21 07:34Note](/article/detail/70560040)[Evolution of Drone Offense and Defense in the Middle East Conflict: Counter-UAV Industry Research

In recent years, repeated conflicts in regions such as the Middle East and Russia-Ukraine have demonstrated that drones are becoming one of the most cost-effective combat tools on the battlefield. From low-cost commercial drones modified into attack platforms to military systems with swarm coordination capabilities, the role of drones in reconnaissance, strike, and attrition warfare continues to strengthen.
Taking Iran-related conflicts as an example, the large-scale use of drones is reshaping traditional offense-defense dynamics: on one hand, attackers can pose a persistent threat to high-value targets at extremely low cost; on the other hand, defensive systems must pay a much higher price for interception and protection. This asymmetric pattern of "low-cost offense, high-cost defense" has rapidly elevated low-altitude security from a tactical issue to a systemic challenge. Against this backdrop, the importance of counter-UAV capabilities has risen significantly. Whether military bases, energy facilities, or critical infrastructure such as airports and power grids, all face persistent threats from low-altitude targets. Traditional air defense systems struggle to effectively counter "low, slow, small" targets, driving the accelerated development of detection and countermeasure systems specifically for drones. Notably, technological paths and application models from the battlefield are rapidly spilling over into the civilian security sector. Methods such as electromagnetic jamming, navigation spoofing, and multi-sensor fusion detection have gradually become integral parts of security systems in key industries. Driven by strengthened regulatory policies, counter-UAV equipment is shifting from deployment in isolated scenarios to broader standardized configurations. Overall, the widespread application of drones is reshaping the offense-defense system, while counter-UAV systems have become a critical component of low-altitude security. This report systematically analyzes the counter-UAV industry from the perspectives of demand, policy, technology paths, and market potential, integrating both war scenarios and industry development.

2026/03/21 04:27Insight](/article/detail/70560039)[Agentic AI's Compute Explosion Is Real—But Value Only Belongs to Those Who Define the Architecture [GTC/OFC 2026 Series]

1. How Agentic AI amplifies compute demand, and whether this growth translates uniformly into profits across the AI stack (software/model layer, chip layer, and physical infrastructure layer)；
2. The scaling challenges of KV cache technology and whether inference service moats are shifting from raw compute to storage optimization；
3. The erosion of GPU market share by custom ASICs, and the architectural competition between CSP in-house silicon ecosystems and NVIDIA.

2026/03/21 00:26Insight](/article/detail/70560022)

- 1
- 2
- 3
- 4

Comments

Published

![No Data](https://static.acecamptech.com/system/empty.svg)

No Data

Publisher

[![](https://image.acecamptech.com/avatar/50524811/1734398740530.jpg?x-oss-process=style/avatar)](/organizer/20510256)

[Faby Luo](/organizer/20510256)

Published 112 Articles

Follow

Latest update

[More>](/organizer/20510256)

- [In-Depth Analysis of Satellite Power Systems: A Panoramic View of a 100-Billion Market and Core Technologies

  2026/03/21 14:43](/article/detail/70560045)
- [Evolution of Drone Offense and Defense in the Middle East Conflict: Counter-UAV Industry Research

  2026/03/21 04:27](/article/detail/70560039)
- [Decoding Electric Propulsion for LEO Satellites: Technology, Industry Progress, and the CNY 10 Billion Opportunity

  2026/03/20 15:07](/article/detail/70560032)

![img](https://static.acecamptech.com/system/posters/en_article_poster.png)

Related Radars

[Hot Radars >](/radars)

- [总结最近1个月专家对存储行业的观点，争议和共识，投资机会和风险

  已关注雷达](/radars?monitor_id=c59d4783-4c4e-5c92-b477-95b44c579834)

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
