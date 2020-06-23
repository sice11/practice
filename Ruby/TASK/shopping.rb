# documents.htmlに則って、買い物アプリを作成

# 今月がボーナス時期かどうかを取得する
# 決められた値以外の場合は繰り返し入力をする
def check
    puts "ボーナス月であれば1を、そうでないなら2を押してください。"
    inputs_flag = true
    while(inputs_flag)
        input = gets.chomp.to_i
        if input == 1 || input == 2
            puts input == 1 ? "ボーナス月ですね。" : "通常給与月ですね。"
            inputs_flag = false
        else
            puts "数字の1か2を入れてください。"
        end
    end
end
check

# 予算の入力
def budget
    puts "予算を入力してください。"
    input_budget = gets.chomp.to_i
end
budget

# 買いたいもののリスト
def list
    want_list = Hash.new()
    puts "買いたいものの名前を入力してください。"
    input_name = gets
    puts "その値段を入力してください。"
    input_value = gets.chomp.to_i
    # want_listにキー（名前）と値（値段）を入力する。
    want_list[:name] = input_name
    want_list[:value] = input_value
end
list