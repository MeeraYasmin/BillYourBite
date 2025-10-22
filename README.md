# BillYourBite Kiro IDE Integration

This directory contains Kiro IDE configurations for enhanced development workflow of the BillYourBite Streamlit application.

## 🚀 Features Integrated

### 📋 Agent Steering
- **billyourbite-standards.md**: Core development standards and guidelines
- **streamlit-optimization.md**: Streamlit-specific best practices (auto-applied to .py files)
- **student-data-guidelines.md**: Student information handling and security guidelines (auto-applied to app.py)

### 🔧 Agent Hooks
- **test-app-on-save**: Automatically tests the app when app.py is saved
- **validate-menu-data**: Validates CSV data integrity when mess_menu.csv is modified
- **manual-performance-check**: On-demand performance and UX review
- **deploy-readiness-check**: Pre-deployment validation checklist
- **code-review-assistant**: Comprehensive code review following project standards
- **student-data-security**: Manual security review for student information handling
- **student-data-migration**: Helper for student data structure updates

### 🔌 MCP Servers
- **filesystem**: File operations and directory management
- **git**: Version control operations
- **python-tools**: Python code execution and testing
- **memory**: Context and entity management
- **sqlite**: Database operations (disabled by default)
- **web-search**: External search capabilities (requires API key)

### 📝 Spec Templates
- **feature-template.md**: Standard template for new feature specifications (updated for student features)
- **nutrition-info-feature.md**: Example spec for adding nutrition information
- **student-dashboard-feature.md**: Example spec for student spending dashboard

## 🎯 How to Use

### Using Agent Hooks
1. **Automatic Hooks**: Save `app.py` or `mess_menu.csv` to trigger validation
2. **Manual Hooks**: Use Kiro's Agent Hooks panel or command palette to run:
   - Performance & UX Review
   - Deploy Readiness Check
   - Code Review Assistant
   - Student Data Security Check
   - Student Data Migration Helper

### Creating Feature Specs
1. Copy `specs/feature-template.md` to create new feature specs
2. Fill in requirements and implementation details
3. Use `#[[file:filename]]` to reference project files
4. Iterate with Kiro on design and implementation

### MCP Server Usage
- Most servers are auto-configured and ready to use
- Enable/disable servers in `settings/mcp.json`
- Add API keys for external services (like web-search)

## 🛠️ Development Workflow

1. **Feature Planning**: Create spec using template
2. **Development**: Code with steering guidelines active
3. **Testing**: Automatic validation on save
4. **Review**: Use manual hooks for comprehensive checks
5. **Deploy**: Run readiness check before deployment

## 📊 Project Structure
```
├── app.py              # Main Streamlit application (updated)
├── mess_menu.csv       # Menu data source
└── .kiro/
    ├── steering/       # Development guidelines
    │   ├── billyourbite-standards.md
    │   ├── streamlit-optimization.md
    │   └── student-data-guidelines.md
    ├── hooks/          # Automated workflows
    │   ├── test-app-on-save.json
    │   ├── validate-menu-data.json
    │   ├── manual-performance-check.json
    │   ├── deploy-readiness-check.json
    │   ├── code-review-assistant.json
    │   ├── student-data-security.json
    │   └── student-data-migration.json
    ├── settings/       # MCP and other configurations
    │   └── mcp.json
    ├── specs/          # Feature specifications
    │   ├── feature-template.md
    │   ├── nutrition-info-feature.md
    │   └── student-dashboard-feature.md
    └── README.md       # This file
```

## 🔄 Customization
- Modify steering files to update development standards
- Add new hooks for project-specific workflows
- Configure additional MCP servers as needed
- Create custom spec templates for different feature types
