def list
    inputs_flag2 = true
    want_list = Hash.new()
    while(inputs_flag2)
        puts "買いたいものの名前を入力。終わる場合はendを入力。"
        input_name = gets
        if input_name = "end"
            puts "入力を終了します。"
            inputs_flag2 = false
        else
            input_value = gets.chomp.to_i
            want_list[:name] = input_name
            want_list[:value] = input_value
        end
    end
    puts want_list
end
list