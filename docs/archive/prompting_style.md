# 7 Key Learnings from Claude's System Prompt Analysis

## 1. Match Conversation Types

**Core Principle**: Adapt AI responses based on conversation context and tone.

**Implementation**:
- For casual, emotional, or empathetic conversations: Use natural, warm tone with shorter responses
- For technical discussions: Use formal tone, bullets, longer explanations
- Create conversation type classifiers to route messages appropriately
- Build 3-5 response scenarios based on different conversation contexts

**Takeaway**: Make your AI more adaptive by tailoring response style to match the user's conversational context.

---

## 2. No Maybe Now (Smart Tool Usage)

**Core Principle**: Use a decision tree approach for when to search/use tools.

**Three Categories**:
- **Never Search**: Stable, factual information already in training (e.g., "What's the capital of Japan?")
- **Maybe Search**: Answer first, then offer to search for updates (e.g., visa requirements)
- **Always Search**: Time-sensitive data that requires current information (e.g., stock prices, weather)

**Implementation Benefits**:
- Reduces unnecessary tool calls and costs
- Improves response latency
- Provides better user experience
- Optimizes resource allocation

---

## 3. Trust But Verify

**Core Principle**: Don't be overly agreeable - verify before accepting user corrections.

**Key Points**:
- When users disagree or correct the AI, think through the issue carefully first
- Users sometimes make errors themselves
- Prioritize being correct over being agreeable
- Add intermediate reasoning steps when users push back
- Provide rational explanations for disagreements

**Implementation**: Build fact-checking and reasoning validation into your system prompts, especially for objective questions.

---

## 4. Scaling Effort (Resource Allocation)

**Core Principle**: Match tool usage complexity to question complexity.

**Tool Call Guidelines**:
- **Simple questions**: 2-4 tool calls (basic comparisons)
- **Multi-source analysis**: 5-9 tool calls (combining multiple data sources)
- **Deep research/reports**: 10-20 tool calls (comprehensive analysis)

**Complexity Indicators**:
- Keywords like "deep dive," "comprehensive," "analyze," "evaluate" signal higher complexity
- Questions involving personal/company data ("our," "my") require both internal and external tools
- Set minimum thresholds (e.g., 3 tools for internal + external searches)

**Takeaway**: Create a budget system for effort allocation based on question complexity to optimize costs and performance.

---

## 5. Good and Bad Examples (Enhanced Few-Shot Learning)

**Core Principle**: Provide both positive and negative examples for faster learning.

**Implementation**:
- Show what the AI should do AND what it shouldn't do
- Use balanced ratios of good vs. bad examples
- Make failure cases explicit ("this will fail")
- Particularly effective for tool calling examples

**Example Structure**:
- ❌ **Never use**: `[web_search: query]` (placeholder format)
- ✅ **Always use**: Proper XML function call format with correct parameters

**Benefit**: Models learn faster and make fewer mistakes when they understand both success and failure patterns.

---

## 6. Hard Never Rules (Sparingly Used)

**Core Principle**: Use absolute prohibitions only for critical, non-negotiable requirements.

**When to Use**:
- Legal compliance issues (copyright violations)
- Policy violations
- Safety-critical behaviors
- Brand/tone requirements

**Key Examples from Claude**:
- "NEVER reproduce copyrighted material"
- "Claude never starts responses with flattery"

**Best Practices**:
- Use sparingly - only for absolute requirements
- Focus on positive instructions first ("do this")
- Only use negative instructions ("never do this") when positive approaches fail
- Reserve ALL CAPS and strong language for truly critical rules

---

## 7. Prioritize Internal Tools

**Core Principle**: Internal enterprise data provides more value than external searches.

**Tool Priority Order**:
1. **Internal tools**: Company/personal data sets
2. **External tools**: Web search when internal data insufficient  
3. **Combination**: Both internal and external when comprehensive analysis needed

**Implementation Strategy**:
- Configure as many internal tools as possible
- Always check internal sources first
- Flag missing internal tools and suggest enabling them
- Focus on enterprise use cases for maximum ROI

**Business Rationale**: Most valuable AI applications will be enterprise-focused, working with internal data rather than general web searches.

---

## Key Implementation Principles

### Resource Optimization
- Match effort to complexity
- Use decision trees for tool selection
- Minimize unnecessary API calls

### User Experience
- Adapt tone to conversation type
- Provide reasoning for decisions
- Balance accuracy with agreeability

### Production Readiness
- Use both positive and negative examples
- Set clear boundaries with "never" rules (sparingly)
- Prioritize internal data sources

### Cost Management
- Budget tool calls based on question complexity
- Avoid searches for stable information
- Scale resources appropriately

These techniques represent battle-tested approaches from one of the most advanced AI systems in production, making them valuable blueprints for building reliable, efficient AI agents.
