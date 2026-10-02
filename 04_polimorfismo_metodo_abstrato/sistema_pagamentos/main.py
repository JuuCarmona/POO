from pagamento import Pagamentos
from cartao_credito import Cartao_credito
from boleto import Boleto
from pix import Pix


pagamento1 = Cartao_credito(100,'12345')
pagamento2 = Boleto(200,'Julia Carmona Guedes Guimarães', 6371554413346)
pagamento3 = Pix(150,'jucgguimares@icloud.com')

pagamento1.exibir_pagamento()
pagamento2.exibir_pagamento()
pagamento3.exibir_pagamento()
