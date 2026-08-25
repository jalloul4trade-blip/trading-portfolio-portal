import streamlit as st
import pandas as pd
from datetime import datetime

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
        {"Account ID": "7701924", "Server": "Givtrade-Live 1", "Account Type": "VIP Institutional", "Deposit": 30000.0, "Balance": 30000.0, "Daily P/L": 1370.0, "Status": "🔴 SUSPENDED"},
        {"Account ID": "8840215", "Server": "Givtrade-Live 2", "Account Type": "VIP Institutional", "Deposit": 30000.0, "Balance": 30000.0, "Daily P/L": 1370.0, "Status": "🔴 SUSPENDED"},
    ])

if 'transactions_db' not in st.session_state:
    st.session_state.transactions_db = [
        {"Transaction ID": "TXN-998241", "Date": "2026-08-20", "Type": "Deposit", "Method": "USDT TRC20", "Amount": "$30,000.00", "Account": "7701924", "Status": "Completed 🟢"},
        {"Transaction ID": "TXN-994102", "Date": "2026-08-15", "Type": "Deposit", "Method": "Bank Wire", "Amount": "$30,000.00", "Account": "8840215", "Status": "Completed 🟢"},
    ]

if 'tickets_db' not in st.session_state:
    st.session_state.tickets_db = [
        {"Ticket ID": "#T-8801", "Date": "2026-08-22", "Subject": "Account Leverage Adjustment", "Department": "Dealing Desk", "Status": "Resolved 🟢"},
        {"Ticket ID": "#T-8802", "Date": "2026-08-24", "Subject": "Server Latency & Routing Inquiry", "Department": "Technical Support", "Status": "Closed 🟢"},
    ]

# --------------------------------------------------
# 🧭 Sidebar Menu
# --------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='color:#00e676; margin-bottom:20px;'><span style='background:#00e676; color:#000; padding:2px 8px; border-radius:6px; font-weight:900;'>G</span> Givtrade</h2>", unsafe_allow_html=True)
    
    st.caption("TRADER'S MENU")
    menu_choice = st.radio(
        label="Trader Menu Options",
        options=["Accounts", "My Profile", "Funds", "Upload Documents", "Messages", "Help Desk", "Economic Calendar", "Request IB"],
        index=0,
        label_visibility="collapsed"
    )

# --------------------------------------------------
# 🔝 Top Navigation Bar
# --------------------------------------------------
prof = st.session_state.profile_data
col_h1, col_h2, col_h3 = st.columns([2, 1, 1.3])
with col_h1:
    st.markdown(f"**Home** / Trader's Menu / **{menu_choice}**")
with col_h3:
    st.markdown(f"""
    <div style='text-align:right; font-size:13px;'>
        <b>{prof['first_name']} {prof['last_name']}</b> <span style='background:#00e676; color:#000; padding:1px 6px; border-radius:4px; font-weight:bold;'>{prof['client_id']}</span>
        &nbsp;|&nbsp; 🇬🇧 &nbsp;|&nbsp; 🚪 <a href='#' style='color:#64748b; text-decoration:none;'>Log out</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='margin:10px 0 25px 0; border:none; border-bottom:1px solid #e2e8f0;'>", unsafe_allow_html=True)

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
        num_rows="dynamic",
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
# 📂 2. My Profile Screen
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
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Communication Language:</td><td style="font-weight:600;">{prof['lang']}</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr><td style="padding:12px 0; color:#64748b;">Country of Residence:</td><td style="font-weight:600;">{prof['country']}</td><td></td></tr>
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
# 📂 3. Funds Screen (Deposit & Withdrawal Management)
# --------------------------------------------------
elif menu_choice == "Funds":
    tab_dep, tab_with, tab_hist = st.tabs(["📥 Deposit Funds", "📤 Withdrawal Request", "📜 Transaction History"])
    
    with tab_dep:
        st.subheader("Deposit Capital into Trading Accounts")
        col_d1, col_d2 = st.columns([1.2, 1])
        with col_d1:
            with st.form("dep_form"):
                acc_target = st.selectbox("Select Target Account", st.session_state.accounts_df['Account ID'].tolist())
                dep_method = st.selectbox("Payment Method", ["USDT (TRC20 / ERC20)", "Bank Wire Transfer (USD / AED)", "Credit / Debit Card", "Crypto (BTC / ETH)"])
                dep_val = st.number_input("Deposit Amount ($)", min_value=100.0, value=5000.0, step=500.0)
                dep_sub = st.form_submit_button("Proceed to Secure Deposit", type="primary")
                if dep_sub:
                    st.session_state.transactions_db.insert(0, {
                        "Transaction ID": f"TXN-{np.random.randint(100000, 999999)}",
                        "Date": datetime.today().strftime('%Y-%m-%d'),
                        "Type": "Deposit",
                        "Method": dep_method,
                        "Amount": f"${dep_val:,.2f}",
                        "Account": acc_target,
                        "Status": "Completed 🟢"
                    })
                    st.success(f"Deposit of ${dep_val:,.2f} registered successfully into account {acc_target}!")
                    st.rerun()
        with col_d2:
            st.markdown("""
            <div class="portal-card">
                <h4>Instant Funding Channels</h4>
                <p style="color:#64748b; font-size:13px; line-height:1.6;">
                    • <b>Crypto / USDT:</b> Instant network confirmation (0.0% fee).<br>
                    • <b>Direct Wire:</b> Same-day institutional liquidity routing.<br>
                    • <b>Cards:</b> Real-time 3D Secure transaction processing.
                </p>
            </div>
            """, unsafe_allow_html=True)

    with tab_with:
        st.subheader("Request Capital Withdrawal")
        with st.form("with_form"):
            w_acc = st.selectbox("From Trading Account", st.session_state.accounts_df['Account ID'].tolist())
            w_method = st.selectbox("Withdrawal Method", ["USDT TRC20 Wallet", "Bank Transfer (SWIFT)", "Credit Card Refund"])
            w_dest = st.text_input("Destination Wallet Address / IBAN", value="TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t")
            w_val = st.number_input("Withdrawal Amount ($)", min_value=50.0, value=2500.0, step=100.0)
            w_sub = st.form_submit_button("Submit Withdrawal Request", type="primary")
            if w_sub:
                st.session_state.transactions_db.insert(0, {
                    "Transaction ID": f"TXN-{np.random.randint(100000, 999999)}",
                    "Date": datetime.today().strftime('%Y-%m-%d'),
                    "Type": "Withdrawal",
                    "Method": w_method,
                    "Amount": f"${w_val:,.2f}",
                    "Account": w_acc,
                    "Status": "Processing 🟡"
                })
                st.success(f"Withdrawal request of ${w_val:,.2f} submitted to finance department.")
                st.rerun()

    with tab_hist:
        st.subheader("Complete Transaction Log")
        st.dataframe(pd.DataFrame(st.session_state.transactions_db), use_container_width=True, hide_index=True)

# --------------------------------------------------
# 📂 4. Upload Documents Screen
# --------------------------------------------------
elif menu_choice == "Upload Documents":
    st.subheader("Identity & Compliance Documentation")
    col_u1, col_u2 = st.columns(2)
    
    with col_u1:
        st.markdown("""
        <div class="portal-card">
            <h4>Primary Identity (Passport / ID)</h4>
            <p style="color:#64748b; font-size:13px;">Document Number: <b>P-7749102-AE</b></p>
            <span class="badge-approved">Approved & Verified 🟢</span>
            <hr style="margin:15px 0; border:none; border-bottom:1px solid #f1f5f9;">
            <p style="font-size:12px; color:#64748b;">Uploaded: 2026-01-14 | Expiry: 2031-01-14</p>
        </div>
        """, unsafe_allow_html=True)

    with col_u2:
        st.markdown("""
        <div class="portal-card">
            <h4>Proof of Address (Utility Bill / Bank Statement)</h4>
            <p style="color:#64748b; font-size:13px;">Address: <b>Dubai, United Arab Emirates</b></p>
            <span class="badge-approved">Approved & Verified 🟢</span>
            <hr style="margin:15px 0; border:none; border-bottom:1px solid #f1f5f9;">
            <p style="font-size:12px; color:#64748b;">Uploaded: 2026-01-14 | Verified by Compliance</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### Upload Additional Documentation")
    st.file_uploader("Select PDF or Image file", type=["pdf", "png", "jpg"])

# --------------------------------------------------
# 📂 5. Messages & Notifications Screen
# --------------------------------------------------
elif menu_choice == "Messages":
    st.subheader("Secure Client Inbox & System Alerts")
    
    messages = [
        {"Sender": "Dealing Desk", "Subject": "Weekly Account Performance Statement", "Date": "2026-08-24 09:00", "Priority": "Normal 🟢"},
        {"Sender": "Risk Management", "Subject": "Margin Level Health Confirmation (93%)", "Date": "2026-08-22 14:30", "Priority": "Important 🔵"},
        {"Sender": "Givtrade System", "Subject": "MT5 Server Bridge Routine Maintenance Completed", "Date": "2026-08-18 22:00", "Priority": "System ⚪"}
    ]
    st.dataframe(pd.DataFrame(messages), use_container_width=True, hide_index=True)

# --------------------------------------------------
# 📂 6. Help Desk Screen
# --------------------------------------------------
elif menu_choice == "Help Desk":
    st.subheader("Institutional Support Desk")
    col_t1, col_t2 = st.columns([1.2, 1])
    
    with col_t1:
        st.markdown("#### Active Support Tickets")
        st.dataframe(pd.DataFrame(st.session_state.tickets_db), use_container_width=True, hide_index=True)
    
    with col_t2:
        st.markdown("#### Open New Support Request")
        with st.form("ticket_form"):
            t_sub = st.text_input("Ticket Subject")
            t_dept = st.selectbox("Department", ["Dealing Desk & Execution", "Technical Support & VPS", "Finance & Settlements", "Compliance"])
            t_msg = st.text_area("Message Details")
            t_btn = st.form_submit_button("Submit Ticket", type="primary")
            if t_btn and t_sub:
                st.session_state.tickets_db.insert(0, {
                    "Ticket ID": f"#T-{np.random.randint(1000, 9999)}",
                    "Date": datetime.today().strftime('%Y-%m-%d'),
                    "Subject": t_sub,
                    "Department": t_dept,
                    "Status": "Open 🟢"
                })
                st.success("Support ticket created successfully!")
                st.rerun()

# --------------------------------------------------
# 📂 7. Economic Calendar Screen
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
# 📂 8. Request IB Screen (Introducing Broker Portal)
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
