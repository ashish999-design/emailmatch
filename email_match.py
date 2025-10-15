import pandas as pd

# 1️⃣ Read both files
df_may1_19 = pd.read_csv('april14-30.csv')
df_may20_july11 = pd.read_csv('may1-todayall.csv')

# 2️⃣ Get unique email list from may1-19.csv
email_list = df_may1_19['メールアドレス'].dropna().unique().tolist()

# 3️⃣ Prepare results list
results = []

# 4️⃣ Count occurrences for each email address
for email in email_list:
    count = df_may20_july11['本文'].apply(lambda x: email in str(x)).sum()
    if count > 0:
        results.append({'メールアドレス': email, '件数': count})

# 5️⃣ Create summary DataFrame
summary_df = pd.DataFrame(results)

# 6️⃣ Sort by 件数 descending
summary_df = summary_df.sort_values(by='件数', ascending=False)

# 7️⃣ Save output to a file
output_file = 'matched_summary_per_email.csv'
summary_df.to_csv(output_file, index=False, encoding='utf-8-sig')

# 8️⃣ Optional: also print 件数 summary
print(f"✅ Summary saved to {output_file}")
print(summary_df)
