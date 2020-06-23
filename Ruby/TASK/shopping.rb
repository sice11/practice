# documents.htmlに則って、買い物アプリを作成

class Shopping

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
                # 買いたいものの値段を合計したものを変数へ
                @sum = want_list.values.inject(:+)
            else
                puts "入力を終了します。"
                inputs_flag2 = false
            end
        end
        puts @sum
    end

    # 予算と実費の計算
    def budget
        puts "予算を入力してください。"
        input_budget = gets.chomp.to_i
        # 予算と実費の計算
        calc = input_budget - @sum
        print "今月の残りは" , calc , "です。"
    end

end

# クラス内の実行
shopping = Shopping.new
# ボーナス月の判定
shopping.check
# 買いたいものリスト作成
shopping.list
# 残金の計算
shopping.budget