    # 買いたいもののリストの動作確認
    def list
        inputs_flag2 = true
        want_list = Array.new
        while(inputs_flag2)
            puts "買いたいものの値段を入力しますか？する場合はcon、しない場合はendを入力してください。"
            input_switch = gets.chomp
            if input_switch != "end"
                puts "値段を入力してください。"
                input_value = gets.chomp.to_i
                want_list.push(input_value)
                # 買いたいものの値段を合計したものを変数へ
                @sum = want_list.sum
            else
                puts "入力を終了します。"
                inputs_flag2 = false
            end
        end
        puts @sum
    end

    list
