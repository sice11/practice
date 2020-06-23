# documents.htmlに則って、買い物アプリを作成

# 今月がボーナス時期かどうかを取得する
# 決められた値以外の場合は繰り返し入力をする
def check
    puts "数字の1か2を入れてください。"
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