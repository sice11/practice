# documents.htmlに則って、買い物アプリを作成

# 今月がボーナス時期かどうかを取得する
# 決められた値以外の場合は繰り返し入力をする
def check
    input = gets.chomp.to_i
    case input
        when 1
            puts "ボーナス月ですね。"
        when 2
            puts "通常給与月ですね。"
        else
            input_flag = true
            while (input_flag)
                case input
                    when 1
                        puts "ボーナス月ですね。"
                        input_flag = false
                    when 2
                        puts "通常給与月ですね。"
                        input_flag = false
                    else
                        puts "数字の1または2を入力してください"
                        input = gets.chomp.to_i
                end
            end
    end
end
check