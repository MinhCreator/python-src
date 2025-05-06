from time import sleep
import random

def random_stats(name_player: str):
   #random buff
   mutiple = random.randint(1, 4)
   steal = random.randint(10, 30)
   turn = random.randint(1, 3)
   time = random.randint(1, 10)
   minus_score_enermy = random.randint(0, 25)
   supports_turn = random.randint(1, 3)
   exempt_skill = random.randint(1, 5)
   improve_skill = random.randint(1, 4)
   minus_point_percent = random.randint(0, 65)
   plus_effect = round(random.uniform(0.1, 0.4), 2)
   
   #random debuff
   take_score = random.randint(1, 30)
   non_support = random.randint(1, 3)
   limit_used = random.randint(1, 5)
   minus_point_percent2 = random.randint(1, 25)
   steal_member = random.randrange(15, 40)

   buff_skills = [
      
      f"  + nhân đôi số điểm nhận được: {mutiple}x lần", 
      f"  + cướp điểm của team bạn: {steal} điểm", 
      f"  + số lượt trả lời câu hỏi được cộng thêm: {turn} lượt", 
      f"  + thời gian trả lời câu hỏi được cộng thêm {time}s", 
      f"  + trừ đi {minus_score_enermy} điểm trong tổng điểm của team địch", 
      f"  + vô hiệu hóa skills của team địch ở lượt tiếp theo", 
      f"  + được {supports_turn} lần trợ giúp từ team", 
      f"  + trừ bớt {minus_point_percent}% điểm của team địch",
      f"  + miễn 0.{exempt_skill}% các skill bất lợi của địch",
      f"  + team địch đã chọc giận bạn, mọi hiệu ứng bất lợi mà bạn gây ra cho team địch tăng lên 0.{improve_skill}%",
      f"  + (hôm nay bạn quá may mắn) mọi hiệu ứng bất lợi của team địch gây ra cho bạn sẽ được miễn 100%. Đồng thời team địch sẽ là người hứng chịu cộng dồn những hiệu ứng đó",
      "  + bạn được phép bỏ qua câu hỏi trên mà vẫn nhận được điểm của câu hỏi đó",
      f"  + nếu không dùng skill card ở lượt hiện tại thì mọi buff cũng như debuff skill của bạn được cộng thêm {plus_effect}%"
      
      ]
  
   debuff_skills = [
      
      f"  + trừ {take_score} điểm của team và cộng vào cho team bạn", 
      f"  + không nhận được sự trợ giúp của đồng đội trong: {non_support} lượt", 
      f"  + giới hạn sử dụng skill card: {limit_used} lượt", 
      "  + mất quyền trả lời ở lượt tiếp theo", 
      "  + trừ bớt 20% số điểm nhận được", 
      "  + thẻ kĩ năng chỉ được sử dụng được skill card 1 lần", 
      f"  + trừ bớt {minus_point_percent2}% điểm của team khi sử dụng skill card",
      "  + sau khi dùng skill card thì ở lượt tiếp theo mọi hiệu ứng bất lợi của team địch tăng lên 2x",
      "  + (nếu bạn dính thứ này chắc chắn là bạn rất đen) bạn đã bị dính 1 lời nguyền trừ toàn bộ điểm của team về 0 cũng như mọi skill của bạn ở trên sẽ bị vô hiệu hóa và mất lượt trả lời ở lượt tiếp theo",
      "  + sau khi dùng skill card thì ở lượt tiếp theo mọi hiệu ứng bất lợi của team địch tăng lên 0,5%",
      "  + mọi debuff của bạn và team địch sẽ bị cộng dồn và áp dụng cho team của bạn ở lượt tiếp theo",
      "  + (ra đường mà quên xem ngày) bạn phải hoán đổi skill card của bạn với một bạn khác ở trong team địch ở lượt tiếp theo và team địch có quyền chọn ra 1 người để hoán đổi thẻ",
      "  + bạn bị mất lượt trả lời câu hỏi này và ở 2 lượt tiếp theo nếu sử dụng thẻ nhưng buff effect và debuff effect vẫn được áp dụng",
      "  + team của bạn phải hoán đổi điểm nhận được với team địch ở lượt tiếp theo"
      f"  + bạn bị lộ vị trí khi sử dụng skill card khi buộc team bạn phải bỏ ra {steal_member} điểm để chuộc lại bạn"
      ]
   
   quatity_buff = random.randint(1, 4)
   quatity_debuff = random.randint(2, 5)
   random_skills = ["* buff effect: "] + random.sample(buff_skills, quatity_buff) + ["* debuff effect: "] + random.sample(debuff_skills, quatity_debuff)
   
   length = len(random_skills) - 2
   if length > 5:
      print("---bạn đã nhận được thẻ skills legendary---")
      print()
   elif length == 5:
      print("---bạn đã nhận được thẻ skills epic---")
      print()
   elif length <= 4:
      print("---bạn đã nhận được thẻ skills common hoặc uncommon---")
      print()
   elif length < 3:
      print("---bạn đã nhận được thẻ bad skills ---")
      print()
   
   return print(f"------------|player skills|------------       \n{"\n".join(random_skills)}")

def random_time():
   time = random.randint(15, 30)
   return f"* thời gian\n   + thời gian trả lời câu hỏi: {time}s"

def notification(name_player: str):
   import random
   notice = [
      "không phải hôm nay", 
      "do bạn hơi đen", 
      "bạn nhất định sẽ làm được", 
      "bạn là nhất", 
      "thôi xong.....",
      "to be continued",
      "we'll right back",
      "chúc may mắn lần sau",
      "bạn được trời độ",
      "nghiệp cả đấy",
      "bạn đã được game_master buff bẩn",
      "ngu rồi......!",
      "hơi non :))",
      "còn một tí nữa là được rồi......"
      ]
   return f"{random.choice(notice)}"

name_player = input("Enter player name: ")
print()
print(notification(name_player))
print()
print("-----chờ tí nha.....xin đừng làm phiền-----")
print()
sleep(2)
random_stats(name_player)
print()
print(random_time())
print()
sleep(2)
print("-----....Generated player stats!...-----")