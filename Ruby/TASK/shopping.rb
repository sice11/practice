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
    inputs_flag2 = true
    want_list = Hash.new()
    while(inputs_flag2)
        puts "買いたいものの名前を入力。終わる場合はendを入力。"
        input_name = gets.chomp
        if input_name != "end"
            puts "その値段を入力してください。"
            input_value = gets.chomp.to_i
            want_list[input_name] = input_value
        else
            puts "入力を終了します。"
            inputs_flag2 = false
        end
    end
    puts want_list
end
list