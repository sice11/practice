    # 買いたいもののリストのsample
    # issues#33対応
    def list
        inputs_flag2 = true
        want_list = Array.new
        @input_value = 0
        while(inputs_flag2)
            puts "買いたいものの名前を入力。終わる場合はendを入力。"
            input_name = gets.chomp
            if input_name != "end"
                puts "その値段を入力してください。"
                # 買いたいものの値段を合計したものを変数へ
                @input_value = @input_value + gets.chomp.to_i
                # 買いたいものの名前リスト作成
                want_list.push(input_name)
            else
                puts "入力を終了します。"
                puts "入力された買いたいものは。以下となります。"
                puts want_list
                inputs_flag2 = false
            end
        end
        puts @input_value
    end
list