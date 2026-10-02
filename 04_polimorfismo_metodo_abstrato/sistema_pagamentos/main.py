from pagamento import Pagamentos
from cartao_credito import Cartao_credito
from boleto import Boleto
from pix import Pix


pagamento1 = Cartao_credito(100,'12345')
pagamento2 = Boleto(200,'Maria da Silva','000.000.000-00')
pagamento3 = Pix(150,'maria@exemplo.com')

pagamento1.exibir_pagamento()
pagamento2.exibir_pagamento()
pagamento3.exibir_pagamento()
