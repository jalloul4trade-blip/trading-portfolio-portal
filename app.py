import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

# أيقونة التبويب المخصصة بحرفي GT
GT_FAVICON_SVG = """data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>
<rect width='64' height='64' rx='14' fill='%23061a10'/>
<text x='50%' y='54%' dominant-baseline='middle' text-anchor='middle' font-family='Arial Black, sans-serif' font-weight='900' font-size='32' fill='%2300c853'>GT</text>
</svg>"""

st.set_page_config(
    page_title="GT Portal - Client Terminal",
    page_icon=GT_FAVICON_SVG,
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# 🎨 Official Client Portal Styling & GT Branding
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid #1e293b;
    }
    
    .gt-logo-box {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 25px;
    }
    .gt-badge {
        background: linear-gradient(135deg, #022b16 0%, #000000 100%);
        border: 2px solid #00c853;
        color: #00c853;
        font-family: 'Arial Black', sans-serif;
        font-size: 24px;
        font-weight: 900;
        padding: 4px 14px;
        border-radius: 10px;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(0, 200, 83, 0.2);
    }
    .gt-title {
        color: #ffffff;
        font-size: 20px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    .gt-title span {
        color: #00c853;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label {
        font-size: 15px !important;
        font-weight: 600 !important;
        padding: 6px 12px !important;
        color: #cbd5e1 !important;
        border-radius: 8px;
        transition: all 0.2s;
    }
    section[data-testid="stSidebar"] div[data-testid="stRadio"] label:hover {
        color: #00e676 !important;
        background: rgba(255, 255, 255, 0.05);
    }
    
    .portal-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .btn-green {
        background-color: #00c853;
        color: white;
        border-radius: 6px;
        padding: 6px 14px;
        font-weight: 600;
        font-size: 13px;
        display: inline-block;
    }
    .badge-approved {
        background: #ecfdf5;
        color: #059669;
        border: 1px solid #a7f3d0;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 700;
    }
    .download-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .btn-download {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 8px 25px;
        color: #1e293b;
        font-weight: 600;
        font-size: 14px;
        cursor: pointer;
        margin-top: 15px;
        display: inline-block;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 🗄️ Editable Session Database
# --------------------------------------------------
if 'profile_data' not in st.session_state:
    st.session_state.profile_data = {
        "first_name": "Hasan",
        "last_name": "Jalloul",
        "client_id": "22752",
        "dob": "25-05-1987",
        "email": "jalloul4tradefx@gmail.com",
        "phone": "+971586747174",
        "lang": "English",
        "country": "United Arab Emirates"
    }

if 'accounts_df' not in st.session_state:
    st.session_state.accounts_df = pd.DataFrame([
        {"Account ID": "7701924", "Server": "GT-Pro STP", "Account Type": "VIP Institutional", "Deposit": 30000.0, "Balance": 30000.0, "Profit / Loss": 1374.0, "Leverage": "1:10", "Status": "🔴 SUSPENDED"},
        {"Account ID": "8840215", "Server": "GT-Pro STP", "Account Type": "VIP Institutional", "Deposit": 30000.0, "Balance": 30000.0, "Profit / Loss": 1376.0, "Leverage": "1:10", "Status": "🔴 SUSPENDED"},
    ])

if 'user_banks' not in st.session_state:
    st.session_state.user_banks = [
        {
            "bank_name": "First Abu Dhabi Bank (FAB)",
            "account_title": "Hasan Yousef Jalloul",
            "iban": "AE440330000000123456789",
            "account_number": "10408824101",
            "currency": "AED / USD",
            "swift": "FABAAEAD"
        },
        {
            "bank_name": "Emirates Islamic Bank (EIB)",
            "account_title": "Hasan Yousef Jalloul",
            "iban": "AE880240000000987654321",
            "account_number": "40207791402",
            "currency": "AED / USD",
            "swift": "EBILAEAD"
        }
    ]

if 'transactions_df' not in st.session_state:
    st.session_state.transactions_df = pd.DataFrame([
        {"Transaction ID": "TXN-998241", "Date": "2026-08-20", "Type": "Deposit", "Method": "Bank Wire (FAB)", "Amount": "$30,000.00", "Account": "7701924", "Status": "Completed 🟢"},
        {"Transaction ID": "TXN-994102", "Date": "2026-08-15", "Type": "Deposit", "Method": "Bank Wire (Emirates Islamic)", "Amount": "$30,000.00", "Account": "8840215", "Status": "Completed 🟢"},
    ])

# --------------------------------------------------
# 🧭 Sidebar Menu (Includes GT Platform Option)
# --------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="gt-logo-box">
        <span class="gt-badge">GT</span>
        <div class="gt-title">PORTAL<span>.</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='color:#64748b; font-size:12px; font-weight:700; letter-spacing:1px; margin-bottom:8px;'>TRADER'S MENU</p>", unsafe_allow_html=True)
    
    main_nav = st.radio(
        label="Main Section",
        options=["Accounts", "Funds", "GT Platform", "My Profile", "Downloads", "Economic Calendar"],
        index=0,
        label_visibility="collapsed"
    )
    
    funds_sub_choice = "Wallet Accounts"
    if main_nav == "Funds":
        st.markdown("<p style='color:#00e676; font-size:11px; font-weight:700; margin: 10px 0 4px 10px;'>FUNDS MANAGEMENT</p>", unsafe_allow_html=True)
        funds_sub_choice = st.radio(
            label="Funds Submenu",
            options=["Wallet Accounts", "Deposit Funds", "Withdraw Funds", "Transfer Funds", "Transactions History", "Payment Details"],
            index=0,
            label_visibility="collapsed"
        )
    
    st.markdown("<br><hr style='border:none; border-bottom:1px solid #1e293b;'><br>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:12px; font-weight:700; letter-spacing:1px; margin-bottom:8px;'>IB MENU</p>", unsafe_allow_html=True)
    ib_choice = st.checkbox("💼 Request IB")

if ib_choice:
    active_page = "Request IB"
elif main_nav == "Funds":
    active_page = f"Funds - {funds_sub_choice}"
else:
    active_page = main_nav

# --------------------------------------------------
# 🔝 Top Navigation Bar & Action Buttons
# --------------------------------------------------
prof = st.session_state.profile_data

col_top_l, col_top_r = st.columns([1.5, 1.5])
with col_top_l:
    st.markdown(f"<div style='padding-top:8px; font-size:15px;'>☰ &nbsp;&nbsp; <b>Home</b> / Trader's Menu / <b>{active_page}</b></div>", unsafe_allow_html=True)

with col_top_r:
    st.markdown(f"""
    <div style='text-align:right; font-size:14px; display:flex; align-items:center; justify-content:flex-end; gap:18px;'>
        <span><b>{prof['first_name']} {prof['last_name']}</b> <span style='background:#00c853; color:#000; padding:2px 7px; border-radius:4px; font-weight:bold;'>{prof['client_id']}</span></span>
        <span>🇬🇧</span>
        <span>✉️ Messages</span>
        <span>🎧 Help Desk</span>
        <span>🚪 <a href='#' style='color:#64748b; text-decoration:none;'>Log out</a></span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# --------------------------------------------------
# 📂 1. Accounts Screen
# --------------------------------------------------
if active_page == "Accounts":
    
    @st.dialog("Trading Account Specifications & Credentials")
    def show_acc_details(acc_id):
        acc = next(a for a in st.session_state.accounts_df.to_dict('records') if str(a['Account ID']) == str(acc_id))
        st.markdown(f"""
        <div style='background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:18px;'>
            <table style='width:100%; border-collapse:collapse; font-size:14px;'>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Account ID / Login:</td><td><b>{acc['Account ID']}</b></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Trading Server:</td><td><b style='color:#00c853;'>{acc['Server']} (Real Live)</b></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Platform:</td><td><b>MetaTrader 5 (MT5)</b></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Account Leverage:</td><td><b>{acc.get('Leverage', '1:10')}</b></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Account Classification:</td><td><b>{acc['Account Type']}</b></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Account Currency:</td><td><b>USD ($)</b></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Trading Password:</td><td><span style='font-family:monospace; font-size:16px;'>••••••••••••</span></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Investor (Read-Only) Password:</td><td><span style='font-family:monospace; font-size:16px;'>••••••••••••</span></td></tr>
                <tr style='border-bottom:1px solid #f1f5f9;'><td style='padding:10px 0; color:#64748b;'>Execution Model:</td><td><b>DMA / STP Tier-1</b></td></tr>
                <tr><td style='padding:10px 0; color:#64748b;'>Account Health / Status:</td><td><b>{acc['Status']}</b></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.button("🔑 Change Master Password", use_container_width=True)
        with col_m2:
            st.button("👁️ Change Investor Password", use_container_width=True)

    @st.dialog("➕ Add New Trading Account")
    def open_add_acc_dialog():
        with st.form("add_acc_direct_form"):
            c_a1, c_a2 = st.columns(2)
            with c_a1:
                n_id = st.text_input("Account ID", value=str(np.random.randint(9000000, 9999999)))
                n_srv = st.selectbox("Server", ["GT-Pro STP", "GT-Live 1", "GT-Live 2", "GT-Demo 1"])
                n_type = st.selectbox("Account Type", ["VIP Institutional", "Classic STP", "Swap-Free Gold"])
            with c_a2:
                n_dep = st.number_input("Deposit ($)", min_value=100.0, value=10000.0, step=1000.0)
                n_bal = st.number_input("Balance ($)", min_value=0.0, value=10000.0, step=1000.0)
                n_pl = st.number_input("Profit / Loss ($)", value=0.0, step=100.0)
            
            n_lev = st.selectbox("Leverage", ["1:10", "1:20", "1:50", "1:100"], index=0)
            
            btn_save = st.form_submit_button("Save & Add Account", type="primary", use_container_width=True)
            if btn_save and n_id:
                new_entry = {
                    "Account ID": str(n_id),
                    "Server": n_srv,
                    "Account Type": n_type,
                    "Deposit": float(n_dep),
                    "Balance": float(n_bal),
                    "Profit / Loss": float(n_pl),
                    "Leverage": n_lev,
                    "Status": "🔴 SUSPENDED"
                }
                st.session_state.accounts_df = pd.concat([st.session_state.accounts_df, pd.DataFrame([new_entry])], ignore_index=True)
                st.rerun()

    @st.dialog("Open New Demo Trading Account")
    def open_demo_dialog():
        with st.form("create_demo_form"):
            d_platform = st.selectbox("Trading Platform", ["MetaTrader 5 (MT5)", "MetaTrader 4 (MT4)"])
            d_type = st.selectbox("Account Type", ["Standard STP Demo", "VIP ECN Demo", "Raw Spread Demo"])
            d_lev = st.selectbox("Leverage", ["1:10", "1:100", "1:200", "1:500"], index=0)
            d_bal = st.selectbox("Initial Virtual Deposit ($)", [1000.0, 5000.0, 10000.0, 50000.0, 100000.0], index=2)
            
            sub_demo = st.form_submit_button("Create Demo Account", type="primary", use_container_width=True)
            if sub_demo:
                new_acc_id = str(np.random.randint(7000000, 8999999))
                new_row = {
                    "Account ID": new_acc_id,
                    "Server": "GT-Demo 1",
                    "Account Type": d_type,
                    "Deposit": float(d_bal),
                    "Balance": float(d_bal),
                    "Profit / Loss": 0.0,
                    "Leverage": d_lev,
                    "Status": "🟢 ACTIVE DEMO"
                }
                st.session_state.accounts_df = pd.concat([st.session_state.accounts_df, pd.DataFrame([new_row])], ignore_index=True)
                st.rerun()

    c_head1, c_head_btn1, c_head_btn2 = st.columns([3, 1.2, 1])
    with c_head_btn1:
        if st.button("➕ Open Demo Account", use_container_width=True):
            open_demo_dialog()

    with c_head_btn2:
        if st.button("💳 Deposit Funds", type="primary", use_container_width=True):
            st.info("Select Deposit Funds from the sidebar menu to proceed.")

    st.markdown("<br>", unsafe_allow_html=True)

    df = st.session_state.accounts_df.copy()
    
    df['Deposit'] = pd.to_numeric(df['Deposit'], errors='coerce').fillna(0)
    df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce').fillna(0)
    df['Profit / Loss'] = pd.to_numeric(df['Profit / Loss'], errors='coerce').fillna(0)
    
    df['Calculated Equity'] = df['Balance'] + df['Profit / Loss']
    df['Total Net P/L'] = df['Calculated Equity'] - df['Deposit']
    
    tot_deposit = df['Deposit'].sum()
    tot_equity = df['Calculated Equity'].sum()
    tot_pl = df['Profit / Loss'].sum()
    tot_net_growth = df['Total Net P/L'].sum()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Deposits", f"${tot_deposit:,.2f}")
    m2.metric("Live Equity", f"${tot_equity:,.2f}")
    m3.metric("Profit / Loss", f"${tot_pl:+,.2f}", f"{(tot_pl/tot_deposit)*100:+.2f}%" if tot_deposit > 0 else "0.00%")
    m4.metric("Total Cumulative Net P/L", f"${tot_net_growth:+,.2f}", f"{(tot_net_growth/tot_deposit)*100:+.2f}%" if tot_deposit > 0 else "0.00%")

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_mat_t, col_mat_sel = st.columns([2.5, 1.2])
    with col_mat_t:
        st.subheader("Trading Accounts Matrix")
    with col_mat_sel:
        acc_choice = st.selectbox("View Account Credentials / Details", ["Select Account..."] + df['Account ID'].tolist())
        if acc_choice != "Select Account...":
            show_acc_details(acc_choice)

    edited_df = st.data_editor(
        st.session_state.accounts_df,
        num_rows="fixed",
        use_container_width=True,
        column_config={
            "Deposit": st.column_config.NumberColumn("Deposit ($)", format="$%.2f"),
            "Balance": st.column_config.NumberColumn("Balance ($)", format="$%.2f"),
            "Profit / Loss": st.column_config.NumberColumn("Profit / Loss ($)", format="$%.2f"),
            "Status": st.column_config.SelectboxColumn("Status", options=["🔴 SUSPENDED", "🟢 ACTIVE", "🟢 ACTIVE DEMO", "🟡 PENDING"]),
            "Server": st.column_config.SelectboxColumn("Server", options=["GT-Pro STP", "GT-Live 1", "GT-Live 2", "GT-Demo 1"]),
            "Leverage": st.column_config.SelectboxColumn("Leverage", options=["1:10", "1:20", "1:50", "1:100"]),
            "Account Type": st.column_config.SelectboxColumn("Account Type", options=["VIP Institutional", "Classic STP", "Swap-Free Gold", "Standard STP Demo", "VIP ECN Demo"])
        }
    )

    if not edited_df.equals(st.session_state.accounts_df):
        st.session_state.accounts_df = edited_df
        st.rerun()

    c_sp, c_btn = st.columns([12, 1])
    with c_btn:
        if st.button("➕", key="btn_add_acc_pop"):
            open_add_acc_dialog()

    st.markdown("---")
    st.subheader("Calculated Equity & Risk Summary")
    summary_view = pd.DataFrame({
        "Account ID": df['Account ID'],
        "Server": df['Server'],
        "Leverage": df.get('Leverage', '1:10'),
        "Calculated Equity": df['Calculated Equity'].map('${:,.2f}'.format),
        "Profit / Loss": df['Profit / Loss'].map('{:+,.2f}$'.format),
        "Total Profit / Loss": df['Total Net P/L'].map('{:+,.2f}$'.format),
        "ROI (%)": ((df['Total Net P/L'] / df['Deposit']) * 100).map('{:+.2f}%'.format),
        "Status": df['Status']
    })
    st.dataframe(summary_view, use_container_width=True, hide_index=True)

# --------------------------------------------------
# 📂 2. GT Platform (TradingView Gateway with Modal)
# --------------------------------------------------
elif active_page == "GT Platform":
    st.subheader("GT Institutional Trading Terminal")
    
    st.markdown("""
    <div class="portal-card" style="text-align: center; padding: 40px 20px;">
        <h2 style="color: #0f172a; margin-bottom: 10px;">Direct Market Execution & Advanced Charting</h2>
        <p style="color: #64748b; font-size: 15px; max-width: 600px; margin: 0 auto 25px;">
            Access real-time institutional price action, multi-timeframe analytics, and market liquidity depth powered by TradingView.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    @st.dialog("External Platform Navigation")
    def confirm_navigation():
        st.markdown("""
        <div style='text-align: center; padding: 10px 0;'>
            <h3 style='color: #0f172a; margin-bottom: 12px;'>Leaving GT Client Portal</h3>
            <p style='color: #64748b; font-size: 14px; line-height: 1.6;'>
                You are about to launch the <b>GT Institutional Charting Engine</b> in a new secure browser tab powered by <b>TradingView</b>.
            </p>
            <p style='color: #00c853; font-size: 13px; font-weight: 700;'>
                Do you wish to proceed?
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_yes, col_no = st.columns(2)
        with col_yes:
            st.markdown("""
            <a href="https://www.tradingview.com/chart/" target="_blank" style="text-decoration: none;">
                <div style="background-color: #00c853; color: white; text-align: center; padding: 10px; border-radius: 8px; font-weight: 700; font-size: 14px;">
                    Yes, Proceed to Platform
                </div>
            </a>
            """, unsafe_allow_html=True)
        with col_no:
            if st.button("Cancel & Return", use_container_width=True):
                st.rerun()

    col_btn_center1, col_btn_center2, col_btn_center3 = st.columns([1, 1.2, 1])
    with col_btn_center2:
        if st.button("🚀 Launch GT Platform Terminal", type="primary", use_container_width=True):
            confirm_navigation()

# --------------------------------------------------
# 📂 3. Funds - Wallet Accounts
# --------------------------------------------------
elif active_page == "Funds - Wallet Accounts":
    st.subheader("Wallet Accounts")
    wallet_df = pd.DataFrame([
        {"Account Type": "Wallet", "Wallet Number": "10208", "Currency": "USD", "Balance": "$0.00", "Action": "🗂️ History"}
    ])
    st.dataframe(wallet_df, use_container_width=True, hide_index=True)

# --------------------------------------------------
# 📂 4. Funds - Deposit Funds
# --------------------------------------------------
elif active_page == "Funds - Deposit Funds":
    st.subheader("Deposit Capital via Direct Bank Wire")
    col_d1, col_d2 = st.columns([1.2, 1])
    
    bank_names = [b['bank_name'] for b in st.session_state.user_banks]
    with col_d1:
        with st.form("dep_bank_form"):
            acc_target = st.selectbox("Select Target Account", st.session_state.accounts_df['Account ID'].tolist())
            selected_bank_name = st.selectbox("Select Sending / Receiving Bank", bank_names)
            dep_val = st.number_input("Deposit Amount ($)", min_value=100.0, value=10000.0, step=1000.0)
            dep_ref = st.text_input("Bank Transfer Reference / Note", value=f"GT-{prof['client_id']}")
            
            dep_sub = st.form_submit_button("Confirm Bank Wire Deposit", type="primary")
            if dep_sub:
                new_row = pd.DataFrame([{
                    "Transaction ID": f"TXN-{np.random.randint(100000, 999999)}",
                    "Date": datetime.today().strftime('%Y-%m-%d'),
                    "Type": "Deposit",
                    "Method": f"Bank Wire ({selected_bank_name})",
                    "Amount": f"${dep_val:,.2f}",
                    "Account": acc_target,
                    "Status": "Completed 🟢"
                }])
                st.session_state.transactions_df = pd.concat([new_row, st.session_state.transactions_df], ignore_index=True)
                
                idx = st.session_state.accounts_df.index[st.session_state.accounts_df['Account ID'] == acc_target].tolist()[0]
                st.session_state.accounts_df.at[idx, 'Deposit'] += dep_val
                st.session_state.accounts_df.at[idx, 'Balance'] += dep_val
                
                st.success(f"Deposit of ${dep_val:,.2f} confirmed and added to Account {acc_target}!")
                st.rerun()

    with col_d2:
        curr_b = next(b for b in st.session_state.user_banks if b['bank_name'] == selected_bank_name)
        st.markdown(f"""
        <div class="portal-card">
            <h4 style="margin-top:0;">{curr_b['bank_name']} Details</h4>
            <p style="color:#64748b; font-size:13px; line-height:1.7;">
                • <b>Account Name:</b> {curr_b['account_title']}<br>
                • <b>Account Number:</b> {curr_b['account_number']}<br>
                • <b>IBAN:</b> {curr_b['iban']}<br>
                • <b>SWIFT / BIC:</b> {curr_b['swift']}<br>
                • <b>Currency:</b> {curr_b['currency']}<br>
                • <b>Processing Time:</b> Same-day Institutional Wire
            </p>
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# 📂 5. Funds - Withdraw Funds
# --------------------------------------------------
elif active_page == "Funds - Withdraw Funds":
    st.subheader("Request Capital Withdrawal to Bank Account")
    bank_names = [b['bank_name'] for b in st.session_state.user_banks]
    with st.form("with_bank_form"):
        w_acc = st.selectbox("From Trading Account", st.session_state.accounts_df['Account ID'].tolist())
        w_bank = st.selectbox("Select Destination Bank", bank_names)
        
        b_info = next(b for b in st.session_state.user_banks if b['bank_name'] == w_bank)
        st.info(f"Transferring to: {b_info['bank_name']} | IBAN: {b_info['iban']}")
        
        w_val = st.number_input("Withdrawal Amount ($)", min_value=100.0, value=5000.0, step=500.0)
        w_sub = st.form_submit_button("Submit Bank Wire Withdrawal", type="primary")
        if w_sub:
            new_row = pd.DataFrame([{
                "Transaction ID": f"TXN-{np.random.randint(100000, 999999)}",
                "Date": datetime.today().strftime('%Y-%m-%d'),
                "Type": "Withdrawal",
                "Method": f"Bank Wire ({w_bank})",
                "Amount": f"${w_val:,.2f}",
                "Account": w_acc,
                "Status": "Processing 🟡"
            }])
            st.session_state.transactions_df = pd.concat([new_row, st.session_state.transactions_df], ignore_index=True)
            st.success(f"Withdrawal request of ${w_val:,.2f} sent to settlements department.")
            st.rerun()

# --------------------------------------------------
# 📂 6. Funds - Transfer Funds
# --------------------------------------------------
elif active_page == "Funds - Transfer Funds":
    st.subheader("Internal Capital Transfer")
    with st.form("internal_transfer_form"):
        col_tr1, col_tr2 = st.columns(2)
        with col_tr1:
            tr_from = st.selectbox("Transfer From", ["Wallet (10208)"] + st.session_state.accounts_df['Account ID'].tolist())
        with col_tr2:
            tr_to = st.selectbox("Transfer To", st.session_state.accounts_df['Account ID'].tolist() + ["Wallet (10208)"])
        
        tr_amt = st.number_input("Transfer Amount ($)", min_value=10.0, value=1000.0, step=100.0)
        tr_btn = st.form_submit_button("Execute Transfer", type="primary")
        if tr_btn:
            st.success(f"Successfully transferred ${tr_amt:,.2f} from {tr_from} to {tr_to} instantly.")

# --------------------------------------------------
# 📂 7. Funds - Transactions History
# --------------------------------------------------
elif active_page == "Funds - Transactions History":
    st.subheader("Bank Wire Transactions Log")
    
    bank_names = [b['bank_name'] for b in st.session_state.user_banks]
    
    edited_trans = st.data_editor(
        st.session_state.transactions_df,
        num_rows="fixed",
        use_container_width=True,
        column_config={
            "Type": st.column_config.SelectboxColumn("Type", options=["Deposit", "Withdrawal"]),
            "Status": st.column_config.SelectboxColumn("Status", options=["Completed 🟢", "Processing 🟡", "Pending ⚪", "Rejected 🔴"]),
            "Account": st.column_config.TextColumn("Account"),
            "Amount": st.column_config.TextColumn("Amount"),
            "Date": st.column_config.TextColumn("Date"),
            "Method": st.column_config.TextColumn("Method")
        }
    )

    if not edited_trans.equals(st.session_state.transactions_df):
        st.session_state.transactions_df = edited_trans
        st.rerun()

    c_space, c_add = st.columns([12, 1])
    with c_add:
        show_add_form = st.button("➕", key="btn_add_trans_pop")

    if show_add_form:
        with st.form("add_custom_trans_form"):
            col_tr1, col_tr2, col_tr3 = st.columns(3)
            with col_tr1:
                t_id = st.text_input("Transaction ID", value=f"TXN-{np.random.randint(100000, 999999)}")
                t_date = st.text_input("Date (YYYY-MM-DD)", value=datetime.today().strftime('%Y-%m-%d'))
            with col_tr2:
                t_type = st.selectbox("Type", ["Deposit", "Withdrawal"])
                t_method = st.selectbox("Method", [f"Bank Wire ({b})" for b in bank_names] + ["Bank Wire (Direct)"])
            with col_tr3:
                t_amount = st.text_input("Amount (e.g. $15,000.00)", value="$10,000.00")
                t_acc = st.selectbox("Target Account", st.session_state.accounts_df['Account ID'].tolist())
            
            t_status = st.selectbox("Status", ["Completed 🟢", "Processing 🟡", "Pending ⚪", "Rejected 🔴"])
            
            add_t_btn = st.form_submit_button("Add Transaction", type="primary")
            if add_t_btn:
                new_custom_entry = pd.DataFrame([{
                    "Transaction ID": t_id,
                    "Date": t_date,
                    "Type": t_type,
                    "Method": t_method,
                    "Amount": t_amount,
                    "Account": t_acc,
                    "Status": t_status
                }])
                st.session_state.transactions_df = pd.concat([st.session_state.transactions_df, new_custom_entry], ignore_index=True)
                st.rerun()

# --------------------------------------------------
# 📂 8. Funds - Payment Details
# --------------------------------------------------
elif active_page == "Funds - Payment Details":
    st.subheader("Registered Settlement Bank Accounts")
    st.dataframe(pd.DataFrame(st.session_state.user_banks), use_container_width=True, hide_index=True)
    
    c_sp_b, c_btn_b = st.columns([12, 1])
    with c_btn_b:
        show_add_bank = st.button("➕", key="btn_add_bank_pop")

    if show_add_bank:
        with st.form("add_new_bank_form"):
            nb_name = st.text_input("Bank Name", placeholder="e.g. Abu Dhabi Commercial Bank (ADCB)")
            nb_title = st.text_input("Account Holder Name", value=f"{prof['first_name']} {prof['last_name']}")
            nb_num = st.text_input("Account Number", placeholder="e.g. 1029384756")
            nb_iban = st.text_input("IBAN Number", placeholder="AE...")
            nb_swift = st.text_input("SWIFT / BIC Code", placeholder="e.g. ADCBAEAA")
            nb_curr = st.selectbox("Currency", ["AED / USD", "USD", "AED", "EUR", "GBP"])
            
            add_b_btn = st.form_submit_button("Save Bank Account", type="primary")
            if add_b_btn and nb_name and nb_iban:
                st.session_state.user_banks.append({
                    "bank_name": nb_name,
                    "account_title": nb_title,
                    "iban": nb_iban,
                    "account_number": nb_num,
                    "currency": nb_curr,
                    "swift": nb_swift
                })
                st.rerun()

# --------------------------------------------------
# 📂 9. Downloads Screen
# --------------------------------------------------
elif active_page == "Downloads":
    col_dl1, col_dl2 = st.columns(2)
    
    with col_dl1:
        st.markdown("""
        <div class="download-card">
            <h3 style="margin-top:0; font-size:18px; margin-bottom:20px;">MT5 Windows</h3>
            <svg width="140" height="90" viewBox="0 0 140 90" fill="none">
                <rect x="10" y="5" width="120" height="70" rx="4" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
                <rect x="15" y="10" width="110" height="60" fill="#1e293b"/>
                <path d="M25 45 L45 25 L65 50 L85 30 L105 40" stroke="#00c853" stroke-width="2"/>
                <rect x="55" y="77" width="30" height="8" fill="#94a3b8"/>
                <rect x="45" y="85" width="50" height="3" fill="#64748b"/>
            </svg>
            <br>
            <a href="#" class="btn-download">📥 Download</a>
        </div>
        """, unsafe_allow_html=True)

    with col_dl2:
        st.markdown("""
        <div class="download-card">
            <h3 style="margin-top:0; font-size:18px; margin-bottom:20px;">Mobile IOS</h3>
            <svg width="120" height="90" viewBox="0 0 120 90" fill="none">
                <rect x="35" y="5" width="50" height="80" rx="8" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
                <rect x="40" y="12" width="40" height="66" rx="4" fill="#1e293b"/>
                <path d="M45 50 L55 35 L65 55 L75 40" stroke="#00c853" stroke-width="2"/>
                <circle cx="60" cy="81" r="2" fill="#cbd5e1"/>
            </svg>
            <br>
            <a href="#" class="btn-download">📥 Download</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_dl3, col_dl_empty = st.columns([1, 1])
    with col_dl3:
        st.markdown("""
        <div class="download-card">
            <h3 style="margin-top:0; font-size:18px; margin-bottom:20px;">Mobile Android</h3>
            <svg width="120" height="90" viewBox="0 0 120 90" fill="none">
                <rect x="35" y="5" width="50" height="80" rx="6" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
                <rect x="40" y="10" width="40" height="70" rx="3" fill="#1e293b"/>
                <path d="M45 50 L55 35 L65 55 L75 40" stroke="#00c853" stroke-width="2"/>
            </svg>
            <br>
            <a href="#" class="btn-download">📥 Download</a>
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# 📂 10. My Profile Screen
# --------------------------------------------------
elif active_page == "My Profile":
    col_prof_l, col_prof_r = st.columns([1.3, 1], gap="large")
    
    with col_prof_l:
        st.markdown(f"""
        <div class="portal-card">
            <h3 style="margin-top:0; font-size:18px; margin-bottom:20px;">Profile Information</h3>
            <table style="width:100%; border-collapse:collapse;">
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">First Name:</td><td style="font-weight:600;">{prof['first_name']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Last Name:</td><td style="font-weight:600;">{prof['last_name']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Client ID:</td><td style="font-weight:600;">{prof['client_id']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Date of birth:</td><td style="font-weight:600;">{prof['dob']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Password:</td><td style="font-weight:600;">••••••••</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Email:</td><td style="font-weight:600;">{prof['email']}</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Mobile Number:</td><td style="font-weight:600;">{prof['phone']}</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Communication Language:</td><td style="font-weight:600;">English</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr><td style="padding:12px 0; color:#64748b;">Country of Residence:</td><td style="font-weight:600;">United Arab Emirates</td><td></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("✏️ Profile Settings"):
            with st.form("edit_profile_form"):
                f_name = st.text_input("First Name", value=prof['first_name'])
                l_name = st.text_input("Last Name", value=prof['last_name'])
                c_id = st.text_input("Client ID", value=prof['client_id'])
                d_ob = st.text_input("Date of Birth", value=prof['dob'])
                em = st.text_input("Email", value=prof['email'])
                ph = st.text_input("Mobile Number", value=prof['phone'])
                ct = st.text_input("Country", value=prof['country'])
                save_prof = st.form_submit_button("Save Changes", type="primary")
                if save_prof:
                    st.session_state.profile_data.update({
                        "first_name": f_name, "last_name": l_name, "client_id": c_id,
                        "dob": d_ob, "email": em, "phone": ph, "country": ct
                    })
                    st.success("Profile updated successfully!")
                    st.rerun()

    with col_prof_r:
        st.markdown("""
        <div class="portal-card">
            <div style="background:#ecfdf5; color:#059669; padding:8px 12px; border-radius:6px; font-size:13px; font-weight:600; margin-bottom:20px; border:1px solid #a7f3d0;">
                🟢 Your profile is verified
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="color:#64748b; font-size:14px;">Verification Documents</span>
                <span style="background:#00c853; color:white; padding:2px 8px; border-radius:4px; font-size:12px; font-weight:bold;">Approved</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# 📂 11. Economic Calendar Screen
# --------------------------------------------------
elif active_page == "Economic Calendar":
    st.subheader("High-Impact Market Calendar (GMT+4)")
    calendar_events = [
        {"Time": "16:30", "Currency": "USD", "Event": "Core PCE Price Index (MoM)", "Impact": "🔴 High", "Forecast": "0.2%", "Previous": "0.2%"},
        {"Time": "18:00", "Currency": "USD", "Event": "CB Consumer Confidence", "Impact": "🔴 High", "Forecast": "100.5", "Previous": "100.3"},
        {"Time": "12:00", "Currency": "EUR", "Event": "German Consumer Climate", "Impact": "🟠 Medium", "Forecast": "-18.2", "Previous": "-18.4"},
        {"Time": "18:30", "Currency": "USD", "Event": "Crude Oil Inventories", "Impact": "🟠 Medium", "Forecast": "-1.8M", "Previous": "-4.6M"},
    ]
    st.dataframe(pd.DataFrame(calendar_events), use_container_width=True, hide_index=True)

# --------------------------------------------------
# 📂 12. Request IB Screen
# --------------------------------------------------
elif active_page == "Request IB":
    st.subheader("Introducing Broker (IB) & Partner Portal")
    col_ib1, col_ib2, col_ib3 = st.columns(3)
    col_ib1.metric("Active Sub-Accounts", "14 Accounts", "+2 this month")
    col_ib2.metric("Total Monthly Rebate", "$4,850.00", "+18.5% Growth")
    col_ib3.metric("Volume Generated", "840 Lots", "Institutional Tier 1")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="portal-card">
        <h4>Your Institutional Partner Link</h4>
        <p style="color:#64748b; font-size:13px;">Share your direct partner routing link to onboard sub-accounts automatically:</p>
        <code style="background:#f1f5f9; padding:8px 12px; border-radius:6px; font-size:14px; color:#0f172a;">https://gtportal.com/partner/ref/22752</code>
    </div>
    """, unsafe_allow_html=True)
