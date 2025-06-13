  ````instructions
  // filepath: /mnt/c/Users/Alex/cycle_sniper/.github/instructions/documentation-standards.instructions.md
  ---
  applyTo: "**/docs/**,README.md,USER_GUIDE.md,DEVELOPMENT_README.md,changelog.md,*.md"
  ---

  # Modern Documentation Standards & Operations Instructions
  **Version**: 2.0 | **Framework**: Diátaxis-Enhanced | **Last Updated**: June 2025

  ---

  ## 🚀 Tier 1: Essential Daily Reference (Top 50 Lines)

  ### Quick Decision Matrix

  | I need to... | File Authority | Complexity | Time |
  |--------------|----------------|------------|------|
  | **Add user trading guide** | `USER_GUIDE.md` | Simple | 2-4 min |
  | **Document technical implementation** | `DEVELOPMENT_README.md` | Medium | 5-15 min |
  | **Add troubleshooting info** | `USER_GUIDE.md` | Simple | 2-5 min |
  | **Document architecture change** | `DEVELOPMENT_README.md` + Cross-refs | Complex | 15-30 min |
  | **Update configuration guide** | `USER_GUIDE.md` | Medium | 5-10 min |
  | **Add specialized deep-dive** | `up-down-confirmation.md` | Complex | 10-25 min |

  ### File Hierarchy (Authority Order)
  ```
  1. DEVELOPMENT_README.md    # Technical implementation authority
  2. USER_GUIDE.md           # User experience and trading authority  
  3. up-down-confirmation.md # UP/Down system specialist authority
  4. docs/README.md          # Navigation and structure authority
  5. changelog.md            # Version and feature history authority
  ```

  ### Never Rules (Critical)
  - **NEVER** duplicate content across files (violates single source principle)
  - **NEVER** edit generated files in `dist/` directory
  - **NEVER** create circular cross-references
  - **NEVER** use technical jargon in user-focused docs without explanation
  - **NEVER** exceed 10,000 words per file (performance limit)

  ### Basic Formatting (Essential)
  - 🎯 Objectives | 📊 Data | ⚠️ Warnings | ✅ Approved | ❌ Prohibited
  - Use `filename.md` for file references
  - Maximum 3-level heading hierarchy (H1 → H2 → H3)
  - Internal links: `[Text](filename.md#section)`

  ---

  ## 🎯 Tier 2: Detailed Guidance (Next 100 Lines)

  ### Context-Aware Response Guidelines (Diátaxis Framework)

  #### Tutorials (Getting Started Content)
  - **Purpose**: Learning-oriented, step-by-step guidance
  - **Target**: New users who need to accomplish their first success
  - **Structure**: Linear, ordered steps with clear outcomes
  - **Example**: USER_GUIDE.md Quick Start section

  #### How-To Guides (Problem-Solving Content)  
  - **Purpose**: Goal-oriented, practical solutions
  - **Target**: Users with specific problems to solve
  - **Structure**: Action-oriented with clear steps and alternatives
  - **Example**: USER_GUIDE.md Troubleshooting section

  #### Reference (Information Lookup)
  - **Purpose**: Information-oriented, comprehensive details
  - **Target**: Users who know what they're looking for
  - **Structure**: Structured, searchable, authoritative
  - **Example**: DEVELOPMENT_README.md API documentation

  #### Explanation (Understanding Content)
  - **Purpose**: Understanding-oriented, conceptual background
  - **Target**: Users who want to understand "why" and "how it works"
  - **Structure**: Thematic, discussion-based, context-rich
  - **Example**: up-down-confirmation.md algorithmic explanations

  ### Smart Assessment Protocol (No Maybe Now)

  #### Immediate Action (No Assessment Needed)
  - Single section typo fixes
  - Basic link corrections  
  - Simple formatting updates
  - Standard cross-reference additions

  #### Assess First, Then Act (Maybe)
  For potentially complex changes:
  1. Identify affected files using Decision Matrix
  2. Check cross-reference impact
  3. Proceed with targeted updates

  #### Always Assess (Now)  
  - Multi-file content restructuring
  - New major feature documentation
  - Cross-reference system changes
  - Performance-impacting updates

  ### Content Classification System

  #### User-Focused Content (USER_GUIDE.md)
  - ✅ Installation, setup, configuration
  - ✅ Trading strategies and signal interpretation  
  - ✅ Troubleshooting with actionable solutions
  - ✅ Risk management and best practices
  - ❌ Implementation code or build processes
  - ❌ Internal system architecture

  #### Technical Content (DEVELOPMENT_README.md)
  - ✅ System architecture and implementation  
  - ✅ Development workflow and build processes
  - ✅ API specifications and testing procedures
  - ✅ Performance optimization guidelines
  - ❌ Basic user instructions
  - ❌ Trading strategies without technical context

  #### Specialized Content (up-down-confirmation.md)
  - ✅ Deep algorithmic explanations
  - ✅ Mathematical foundations and analysis
  - ✅ Advanced configuration with technical rationale
  - ✅ Performance benchmarking and optimization
  - ❌ Basic usage instructions
  - ❌ General trading advice

  ### Cross-Reference Standards (Enhanced)
  ```markdown
  # Internal references with alt text for accessibility
  [Configuration Guide](USER_GUIDE.md#configuration "Complete configuration instructions")

  # Section references with descriptive anchors
  [Signal Types](USER_GUIDE.md#signal-types "Understanding DCL and WCL signals")

  # External references with reliability indicators
  [TradingView Pine Script v5](https://tradingview.com/pine-script-docs/ "Official documentation - regularly updated")
  ```

  ---

  ## 🔧 Tier 3: Advanced Features & Implementation

  ### Documentation-as-Code Implementation

  #### Automated Validation Pipeline
  ```yaml
  # .github/workflows/docs-validation.yml
  name: Documentation Validation
  on: [push, pull_request]
  jobs:
    validate-docs:
      runs-on: ubuntu-latest
      steps:
        - name: Check internal links
          run: python scripts/validate_cross_references.py
        - name: Validate formatting
          run: python scripts/validate_formatting.py
        - name: Check accessibility
          run: python scripts/validate_accessibility.py
        - name: Verify file size limits
          run: find docs/ -name "*.md" -exec wc -w {} + | awk '$1 > 10000 {print "File too large: " $2}'
  ```

  #### Documentation Templates
  ```markdown
  <!-- .github/ISSUE_TEMPLATE/documentation-update.md -->
  ## Documentation Update Request

  **Type of Update:**
  - [ ] User guide update (USER_GUIDE.md)
  - [ ] Technical documentation (DEVELOPMENT_README.md)
  - [ ] Specialized system docs (up-down-confirmation.md)
  - [ ] Cross-reference audit needed
  - [ ] New feature documentation

  **Content Type (Diátaxis):**
  - [ ] Tutorial (learning-oriented)
  - [ ] How-to guide (problem-oriented) 
  - [ ] Reference (information-oriented)
  - [ ] Explanation (understanding-oriented)

  **Success Criteria:**
  - [ ] Information is accurate and complete
  - [ ] Follows authoritative source hierarchy
  - [ ] Cross-references are valid and helpful
  - [ ] Accessibility guidelines followed
  ```

  ### Accessibility Improvements

  #### Reduced Visual Complexity (50% Reduction Applied)
  - **Visual Indicator Density**: Maximum 1 visual indicator per paragraph, 3 per section
  - **Hierarchy Indicators**: Use text markers (PRIMARY, SECONDARY) alongside visual cues
  - **Screen Reader Support**: All images require alt text, tables include headers

  ### Performance Considerations

  #### File Size Management
  - **Maximum file size**: 10,000 words per documentation file
  - **Loading time target**: Under 2 seconds on 3G connection
  - **Mobile optimization**: All tables should be responsive, maximum 4 columns
  - **Link density**: Maximum 10 internal links per 1,000 words

  ### Documentation Versioning Strategy

  #### Version Control Integration
  ```bash
  # Documentation version tracking
  git tag -a "docs-v2.0" -m "Documentation Standards 2.0 - Diátaxis Implementation"

  # Branch strategy for documentation
  docs/enhancement          # Major documentation improvements
  docs/hotfix-typos         # Critical fixes
  docs/quarterly-review     # Scheduled quarterly reviews
  ```

  ### Quality Assurance Procedures

  #### Pre-Publication Checklist
  - [ ] **Content Authority**: Correct authoritative file selected
  - [ ] **Cross-References**: All internal links validated and functional
  - [ ] **User Journey**: Content serves intended Diátaxis framework purpose
  - [ ] **Formatting**: Follows reduced visual indicator density and accessibility standards
  - [ ] **Performance**: File size under 10,000 words, loading time under 3 seconds
  - [ ] **Mobile-Friendly**: Tables responsive, code blocks appropriately sized
  - [ ] **Accessibility**: Alt text provided, screen reader compatible

  ## 🔧 Validation Scripts & Report Automation

  ### Quick Commands (Most Used)

  ```bash
  # 🎯 Complete workflow (recommended)
  python scripts/docs.py workflow      # validate → fix → re-validate

  # 📊 Individual operations
  python scripts/docs.py validate      # Generate validation report
  python scripts/docs.py fix           # Apply automated fixes
  python scripts/docs.py status        # Quick status check
  ```

  ### Individual Validation Checks

  ```bash
  python scripts/docs.py format        # Formatting (emojis, headings, code blocks)
  python scripts/docs.py links         # Cross-references (broken links, circular refs)
  python scripts/docs.py accessibility # Accessibility (alt text, color independence)
  python scripts/docs.py framework     # Diátaxis framework compliance
  ```

  ### Advanced Operations

  ```bash
  python scripts/docs.py fix-major     # Major structural fixes (use carefully)

  # Direct script access (if needed)
  python scripts/docs/validate_formatting.py
  python scripts/docs/auto_fix_validation.py --safe-fixes
  ```

  ### Automated Report System

  #### Report Locations
  - **docs/reports/validation-status-current.md** - Current validation status
  - **docs/reports/validation-status-YYYY-MM-DD.md** - Daily validation snapshots
  - **docs/reports/README.md** - Reports index and navigation

  #### Script Organization
  ```
  scripts/
  ├── docs.py                          # Main CLI interface
  └── docs/                           # Validation scripts directory
      ├── README.md                   # Scripts documentation
      ├── validate_formatting.py      # Format validation
      ├── validate_cross_references.py # Link validation
      ├── validate_accessibility.py   # Accessibility validation
      ├── validate_diataxis.py        # Framework validation
      ├── generate_validation_reports.py # Report generation
      ├── auto_fix_validation.py      # Safe automated fixes
      ├── comprehensive_validation_fix.py # Major fixes
      └── fix_headings.py             # Heading-specific fixes
  ```

  ### Package.json Integration

  Add these scripts to package.json:
  ```json
  {
    "scripts": {
      "docs:validate": "python scripts/docs.py validate",
      "docs:fix": "python scripts/docs.py fix", 
      "docs:workflow": "python scripts/docs.py workflow",
      "docs:status": "python scripts/docs.py status"
    }
  }
  ```

  ### Current Validation Status

  Latest automated validation results:
  - **🎨 Formatting**: ✅ PASSED (185 warnings, auto-fixable)
  - **🔗 Cross-References**: ✅ PASSED (33 warnings)
  - **♿ Accessibility**: ✅ PASSED (98 warnings)
  - **📚 Diátaxis Framework**: ✅ PASSED

  **Overall Status**: 🟢 **Excellent** - All validations passing

  **Next Action**: Run `python scripts/docs.py fix` to reduce warning count.

  ### Documentation Update Workflow

  #### Standard Update Process
  1. **Identify Authority** (using Decision Matrix)
  2. **Apply Diátaxis Framework** (tutorial/how-to/reference/explanation)
  3. **Run Pre-Edit Validation** (`python scripts/validate_all.py --pre-check`)
  4. **Update Primary Source** (single source of truth)
  5. **Run Post-Edit Validation** (`python scripts/validate_all.py --post-check`)
  6. **Auto-Fix Common Issues** (`python scripts/auto_fix_validation.py`)
  7. **Generate Updated Reports** (`python scripts/generate_validation_reports.py`)
  8. **Deploy with Validation** (CI/CD pipeline)

  #### Temp Folder Policy

  **Task Progress Documentation:**
  - **All temporary task tracking documents** must be created in `docs/temp/` folder
  - **File naming convention**: `[task-type]_[description]_summary.md`
  - **Purpose**: Track progress, corrections, and improvements for ongoing documentation tasks
  - **Examples**: 
    - `USER_GUIDE_corrections_summary.md`
    - `documentation-standards-improvement-summary.md`
    - `architecture-reorganization-progress.md`

  **Temp Folder Management:**
  - **Regular cleanup**: Review and archive completed tasks monthly
  - **Archive location**: Move completed summaries to `docs/reports/archive/`
  - **Active limit**: Maximum 10 active temp files to prevent clutter
  - **Status tracking**: Include completion status and next actions in each temp file

  ---

  ## 📈 Success Metrics & Continuous Improvement

  ### Quality Metrics
  - **User Journey Success**: 95% task completion rate via documentation
  - **Cross-Reference Integrity**: 100% valid internal links (automated)
  - **Content Completeness**: Zero gaps in critical user workflows
  - **Accessibility Score**: WCAG 2.1 AA compliance (automated testing)
  - **Performance**: <3 second load time, <10MB total documentation size
  - **User Satisfaction**: >4.5/5 rating on documentation clarity

  ### Implementation Roadmap

  #### Immediate (Week 1)
  - [x] Tiered reference structure created
  - [x] Visual indicator density reduced by 50%
  - [x] Quick decision matrix implemented
  - [ ] Deploy automated validation pipeline
  - [ ] Add file size monitoring

  #### Short-term (Month 1)  
  - [ ] Full Diátaxis framework implementation
  - [ ] Create user feedback mechanism
  - [ ] Add accessibility validation automation
  - [ ] Performance optimization

  #### Long-term (Quarter 1)
  - [ ] Interactive documentation guides
  - [ ] Advanced cross-reference automation
  - [ ] Documentation analytics implementation
  - [ ] Mobile-first documentation experience

  ---

  **🎯 Implementation Priority**: Focus on Tier 1 adoption first, then gradually implement Tier 2 and Tier 3 features based on user feedback and documentation maturity.

  **📊 Success Measurement**: Track documentation effectiveness through user task completion rates, reduced support tickets, and improved onboarding success metrics.
  ````
