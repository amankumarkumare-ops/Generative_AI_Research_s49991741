# Generative AI Research - Boon or Bane

## Project Overview

This repository contains research materials for a study titled **"Using Generative AI Tools - Boon or Bane."** The project explores the impact, benefits, and risks of generative AI tools in academic and professional settings. It includes literature reviews, quantitative survey data, qualitative interview data, draft reports, and supplementary media.

## Repository Structure

```
Generative_AI_Research_SID/
│
├── Literature_Review/                 # Literature review materials
│   ├── Journal_Articles/             # Peer-reviewed journal articles
│   ├── Conference_Papers/            # Conference proceedings and papers
│   ├── Books/                         # Book chapters and references
│   └── Newspaper_Articles/            # Newspaper and media articles
│
├── Quantitative_Analysis/             # Quantitative research data
│   ├── Survey_Data/                   # Raw and cleaned survey datasets (CSV, Excel)
│   ├── Analysis_Scripts/              # Python scripts for data analysis
│   ├── Survey_Questions/              # Survey questionnaires and templates
│   └── Analysis_Reports/              # Generated analysis reports and summaries
│
├── Qualitative_Analysis/              # Qualitative research data
│   ├── Interview_Transcripts/         # Transcribed interview recordings
│   ├── Interview_Protocols/           # Interview guides and protocols
│   ├── Consent_Forms/                 # Participant consent forms (RESTRICTED)
│   ├── Analysis_Insights/             # Thematic analysis and insights reports
│   └── Data_Visualisations/           # Charts and visual outputs from qualitative data
│
├── Drafts_Reports/                    # Draft and final research documents
│   ├── Research_Proposals/            # Draft research proposals
│   ├── Conference_Papers/             # Draft conference papers for submission
│   └── Final_Reports/                 # Final research reports
│
├── Additional_Materials/              # Supplementary project materials
│   ├── Information_Sheets/           # Participant information sheets
│   ├── Photos/                        # Project-related photographs
│   └── Media_Files/                   # Other media (audio, video, etc.)
│
├── Project_logbook.txt                # Project logbook for collaborative tracking
└── README.md                          # This file
```

## File Naming Conventions

This repository follows a structured file naming convention to ensure consistency and searchability:

- **Format:** `YYYYMMDD_ProjectName_DocumentType_AuthorInitials_Version.extension`
- **Example:** `20260305_GenAI_SurveyData_AK_v01.csv`
- **Rules:**
  - Use underscores (`_`) to separate metadata elements
  - Use ISO 8601 date format (`YYYYMMDD`)
  - Use version numbers (`v01`, `v02`, etc.) for versioned files
  - Avoid spaces and special characters in filenames
  - Keep filenames under 50 characters where possible
  - Use only alphanumeric characters, dashes, and underscores

For more details on file naming best practices, see [Harvard's File Naming Conventions guide](https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions).

## Access Controls

The following data types require special access controls:

| Data Type | Access Level | Reason |
|-----------|-------------|--------|
| Consent Forms | Restricted | Contains personally identifiable information (PII) |
| Interview Transcripts | Restricted | Contains participant identifiers and sensitive responses |
| Survey Data (raw) | Restricted | May contain identifiable participant responses |
| All other folders | Standard | General research materials |

## How to Navigate

1. Start with `Literature_Review/` for background and context on generative AI research
2. Check `Quantitative_Analysis/` for survey methodology, raw data, and statistical analysis
3. Review `Qualitative_Analysis/` for interview data, thematic analysis, and visualisations
4. See `Drafts_Reports/` for the latest draft and final versions of research outputs
5. Refer to `Additional_Materials/` for supplementary resources

## How to Contribute

### For Team Members

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Generative_AI_Research_SID.git
   ```

2. **Create a new branch for your work:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes and commit with meaningful messages:**
   ```bash
   git add .
   git commit -m "Added cleaned survey data and initial analysis scripts"
   ```

4. **Push your branch and create a Pull Request:**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then open a Pull Request on GitHub for review.

### Commit Message Guidelines

- Use the imperative mood (e.g., "Add", "Update", "Fix")
- Keep the first line under 50 characters
- Include a brief description of what changed and why
- Reference issue numbers if applicable

**Examples:**
- `Add literature review articles from IEEE and ACM`
- `Update survey analysis script with data cleaning steps`
- `Fix formatting in final research report v2`

### Code Review Process

1. All changes must be submitted via Pull Request
2. At least one team member must review and approve the PR
3. Resolve any merge conflicts before merging
4. Delete the feature branch after merging

## License

This project is for academic purposes as part of REIT6811 at the University of Queensland.

## Contact

- **Repository Owner:** [Your Name]
- **Student ID:** [Your 8-digit Student ID]
- **Course:** REIT6811 - Applied Class 6
