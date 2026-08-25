import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

st.set_page_config(
    page_title="Givtrade - Client Portal",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# 🎨 Official Client Portal Styling
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
    section[data-testid="stSidebar"] * {
        color: #94a3b8;
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
    .btn-download:hover {
        background: #f1f5f9;
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
        {"Account ID": "7701924", "Server": "Givtrade-Live 1", "Account Type": "VIP Institutional", "Deposit": 40000.0, "Balance": 40000.0, "Daily P/L": 1370.0, "Status": "🔴 SUSPENDED"},
        {"Account ID": "8840215", "Server": "Givtrade-Live 2", "Account Type": "VIP Institutional", "Deposit": 30000.0, "Balance": 30000.0, "Daily P/L": 1370.0, "Status": "🔴 SUSPENDED"},
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
# 🧭 Sidebar Menu
# --------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='color:#00e676; margin-bottom:20px;'><span style='background:#00e676; color:#000; padding:2px 8px; border-radius:6px; font-weight:900;'>G</span> Givtrade</h2>", unsafe_allow_html=True)
    
    st.caption("TRADER'S MENU")
    menu_choice = st.radio(
        label="Trader Menu Options",
        options=["Accounts", "Funds", "My Profile", "Downloads", "Economic Calendar"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("IB MENU")
    ib_choice = st.checkbox("💼 Request IB")
    if ib_choice:
        menu_choice = "Request IB"

# --------------------------------------------------
# 🔝 Top Navigation Bar & Action Buttons
# --------------------------------------------------
prof = st.session_state.profile_data

col_top_l, col_top_r = st.columns([1.5, 1.5])
with col_top_l:
    st.markdown(f"<div style='padding-top:8px; font-size:14px;'>☰ &nbsp;&nbsp; <b>Home</b> / Trader's Menu / <b>{menu_choice}</b></div>", unsafe_allow_html=True)

with col_top_r:
    st.markdown(f"""
    <div style='text-align:right; font-size:13px; display:flex; align-items:center; justify-content:flex-end; gap:15px;'>
        <span><b>{prof['first_name']} {prof['last_name']}</b> <span style='background:#00e676; color:#000; padding:2px 6px; border-radius:4px; font-weight:bold;'>{prof['client_id']}</span></span>
        <span>🇬🇧</span>
        <span>✉️ Messages</span>
        <span>🎧 Help Desk</span>
        <span>🚪 <a href='#' style='color:#64748b; text-decoration:none;'>Log out</a></span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

# أزرار الإجراءات السريعة العلوية
col_btn1, col_btn2 = st.columns([4, 1.2])
with col_btn2:
    st.markdown("""
    <div style='display:flex; justify-content:flex-end; gap:10px; margin-bottom:20px;'>
        <span style='background:#0f172a; color:white; padding:9px 16px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;'>+ Open Demo Account</span>
        <span style='background:#00c853; color:white; padding:9px 16px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;'>💳 Deposit Funds</span>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# 📂 1. Accounts Screen
# --------------------------------------------------
if menu_choice == "Accounts":
    df = st.session_state.accounts_df.copy()
    
    df['Deposit'] = pd.to_numeric(df['Deposit'], errors='coerce').fillna(0)
    df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce').fillna(0)
    df['Daily P/L'] = pd.to_numeric(df['Daily P/L'], errors='coerce').fillna(0)
    
    df['Calculated Equity'] = df['Balance'] + df['Daily P/L']
    df['Total Net P/L'] = df['Calculated Equity'] - df['Deposit']
    
    tot_deposit = df['Deposit'].sum()
    tot_equity = df['Calculated Equity'].sum()
    tot_daily_pl = df['Daily P/L'].sum()
    tot_net_growth = df['Total Net P/L'].sum()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Deposits", f"${tot_deposit:,.2f}")
    m2.metric("Live Equity", f"${tot_equity:,.2f}")
    m3.metric("Daily P/L", f"${tot_daily_pl:+,.2f}", f"{(tot_daily_pl/tot_deposit)*100:+.2f}%" if tot_deposit > 0 else "0.00%")
    m4.metric("Total Cumulative Net P/L", f"${tot_net_growth:+,.2f}", f"{(tot_net_growth/tot_deposit)*100:+.2f}%" if tot_deposit > 0 else "0.00%")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Trading Accounts Matrix")

    edited_df = st.data_editor(
        st.session_state.accounts_df,
        num_rows="fixed",
        use_container_width=True,
        column_config={
            "Deposit": st.column_config.NumberColumn("Deposit ($)", format="$%.2f"),
            "Balance": st.column_config.NumberColumn("Balance ($)", format="$%.2f"),
            "Daily P/L": st.column_config.NumberColumn("Daily P/L ($)", format="$%.2f"),
            "Status": st.column_config.SelectboxColumn("Status", options=["🔴 SUSPENDED", "🟢 ACTIVE", "🟡 PENDING"]),
            "Server": st.column_config.SelectboxColumn("Server", options=["Givtrade-Live 1", "Givtrade-Live 2", "Givtrade-Pro STP"]),
            "Account Type": st.column_config.SelectboxColumn("Account Type", options=["VIP Institutional", "Classic STP", "Swap-Free Gold"])
        }
    )

    if not edited_df.equals(st.session_state.accounts_df):
        st.session_state.accounts_df = edited_df
        st.rerun()

    c_sp, c_btn = st.columns([12, 1])
    with c_btn:
        show_add_acc = st.button("➕", key="btn_add_acc_pop")

    if show_add_acc:
        with st.form("add_acc_clean_form"):
            c_a1, c_a2, c_a3 = st.columns(3)
            with c_a1:
                n_id = st.text_input("Account ID", value="9920145")
                n_srv = st.selectbox("Server", ["Givtrade-Live 1", "Givtrade-Live 2", "Givtrade-Pro STP"])
            with c_a2:
                n_type = st.selectbox("Type", ["VIP Institutional", "Classic STP", "Swap-Free Gold"])
                n_dep = st.number_input("Deposit ($)", min_value=100.0, value=10000.0, step=1000.0)
            with c_a3:
                n_bal = st.number_input("Balance ($)", min_value=0.0, value=10000.0, step=1000.0)
                n_pl = st.number_input("Daily P/L ($)", value=0.0, step=100.0)
            
            btn_add_acc = st.form_submit_button("Save Account", type="primary")
            if btn_add_acc and n_id:
                new_acc_row = pd.DataFrame([{
                    "Account ID": n_id, "Server": n_srv, "Account Type": n_type,
                    "Deposit": n_dep, "Balance": n_bal, "Daily P/L": n_pl, "Status": "🔴 SUSPENDED"
                }])
                st.session_state.accounts_df = pd.concat([st.session_state.accounts_df, new_acc_row], ignore_index=True)
                st.rerun()

    st.markdown("---")
    st.subheader("Calculated Equity & Risk Summary")
    summary_view = pd.DataFrame({
        "Account ID": df['Account ID'],
        "Server": df['Server'],
        "Calculated Equity": df['Calculated Equity'].map('${:,.2f}'.format),
        "Total Profit / Loss": df['Total Net P/L'].map('{:+,.2f}$'.format),
        "ROI (%)": ((df['Total Net P/L'] / df['Deposit']) * 100).map('{:+.2f}%'.format),
        "Status": df['Status']
    })
    st.dataframe(summary_view, use_container_width=True, hide_index=True)

# --------------------------------------------------
# 📂 2. Downloads Screen
# --------------------------------------------------
elif menu_choice == "Downloads":
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
# 📂 3. My Profile Screen
# --------------------------------------------------
elif menu_choice == "My Profile":
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
# 📂 4. Funds Screen
# --------------------------------------------------
elif menu_choice == "Funds":
    tab_dep, tab_with, tab_banks, tab_hist = st.tabs([
        "📥 Bank Deposit", "📤 Bank Withdrawal", "🏛️ Registered Bank Accounts", "📜 Transaction History"
    ])
    
    bank_names = [b['bank_name'] for b in st.session_state.user_banks]

    with tab_dep:
        st.subheader("Deposit Capital via Direct Bank Wire")
        col_d1, col_d2 = st.columns([1.2, 1])
        
        with col_d1:
            with st.form("dep_bank_form"):
                acc_target = st.selectbox("Select Target Account", st.session_state.accounts_df['Account ID'].tolist())
                selected_bank_name = st.selectbox("Select Sending / Receiving Bank", bank_names)
                dep_val = st.number_input("Deposit Amount ($)", min_value=100.0, value=10000.0, step=1000.0)
                dep_ref = st.text_input("Bank Transfer Reference / Note", value=f"GIV-{prof['client_id']}")
                
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

    with tab_with:
        st.subheader("Request Capital Withdrawal to Bank Account")
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

    with tab_banks:
        st.subheader("Registered Bank Accounts")
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

    with tab_hist:
        st.subheader("Bank Wire Transactions Log")
        
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
# 📂 5. Economic Calendar Screen
# --------------------------------------------------
elif menu_choice == "Economic Calendar":
    st.subheader("High-Impact Market Calendar (GMT+4)")
    calendar_events = [
        {"Time": "16:30", "Currency": "USD", "Event": "Core PCE Price Index (MoM)", "Impact": "🔴 High", "Forecast": "0.2%", "Previous": "0.2%"},
        {"Time": "18:00", "Currency": "USD", "Event": "CB Consumer Confidence", "Impact": "🔴 High", "Forecast": "100.5", "Previous": "100.3"},
        {"Time": "12:00", "Currency": "EUR", "Event": "German Consumer Climate", "Impact": "🟠 Medium", "Forecast": "-18.2", "Previous": "-18.4"},
        {"Time": "18:30", "Currency": "USD", "Event": "Crude Oil Inventories", "Impact": "🟠 Medium", "Forecast": "-1.8M", "Previous": "-4.6M"},
    ]
    st.dataframe(pd.DataFrame(calendar_events), use_container_width=True, hide_index=True)

# --------------------------------------------------
# 📂 6. Request IB Screen
# --------------------------------------------------
elif menu_choice == "Request IB":
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
        <code style="background:#f1f5f9; padding:8px 12px; border-radius:6px; font-size:14px; color:#0f172a;">https://givtrade.com/partner/ref/22752</code>
    </div>
    """, unsafe_allow_html=True)
