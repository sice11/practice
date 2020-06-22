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
            puts "数字の1または2を入力してください"
            while (input != 1 || input != 2)
                case input
                    when 1
                        puts "ボーナス月ですね。"
                    when 2
                        puts "通常給与月ですね。"
                end
            end
    end
end
check