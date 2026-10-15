VBCUA RESPONSIVE UI FIX

This bundle contains replacement UI files for the existing 2-VBCUA project.

Replace these exact paths inside your repository:
1. pages/Home.py
2. utils/helper.py
3. assets/styles/custom.css

Keep app.py and all model/database/analysis files unchanged.

Why these files:
- The original custom.css used fixed heights and overflow:hidden on cards.
- The original CSS forced very large font sizes and line-height:1 on some card paragraphs.
- The original Home.py created 11 columns for the pipeline (six cards and five arrows), causing overflow.
- helper.py used a relative CSS path that depends on the terminal's working directory.
- The replacement Home.py keeps the existing content while arranging pipeline cards in two rows of three.

After replacing files:
1. Save all files.
2. In terminal, cd to 2-VBCUA.
3. Activate your existing virtual environment.
4. Run: python -m streamlit run app.py
5. Test zoom at 100%, 125%, 150%, and 200%.

This bundle changes only presentation/layout and the CSS loader path. It does not change model, scoring, database, audio processing, or PDF logic.
