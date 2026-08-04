# E070INT

## Descrição

Cadastros - Filiais - Parâmetros Integrações

---

## Resumo

- Campos: 71
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IntCom | String(001) | Não | Indicativo se a filial executa integração completa (S/N). |
| IntPar | String(001) | Não | Indicativo se a filial executa integração parcial (S/N). |
| CodCli | Number(009,0) | Sim | Cliente padrão para vendas à vista |
| CodRep | Number(009,0) | Sim | Código do representante padrão |
| FpgVis | Number(002,0) | Sim | Código da forma de pagamento para vendas à vista |
| FpgPra | Number(002,0) | Sim | Código da forma de pagamento para vendas a prazo. |
| CodTns | String(005) | Sim | Código da transação padrão de vendas |
| TnsExt | String(005) | Sim | Código da transação padrão para vendas fora do estado |
| TnsPro | String(005) | Sim | Código da transação de padrão para produtos |
| TnsPex | String(005) | Sim | Código da transação padrão para produtos (fora do estado) |
| TnsSer | String(005) | Sim | Código da transação de padrão para serviços |
| TnsSex | String(005) | Sim | Código da transação padrão para serviços (fora do estado) |
| CodTpt | String(003) | Sim | Código do tipo de título a receber |
| CodCpg | String(006) | Sim | Código da condição de pagamento |
| CodTpr | String(004) | Sim | Código da tabela de preço padrão |
| IndBxt | String(001) | Sim | Indicativo se deverá baixar titulos à vista (S/N) |
| IndBxc | String(001) | Sim | Indicativo se deverá baixar titulos de cheque à vista (S/N) |
| IndDer | String(001) | Não | Indicativo se integra o cadastro de derivações separadamente |
| NumCco | String(014) | Sim | Número da conta interna |
| CodDep | String(250) | Sim | Código do depósito padrão |
| TnsRed | String(005) | Sim | Código da transação padrão para redução Z |
| TnsCob | String(005) | Sim | Código da transação padrão para NF cobrança |
| TnsCex | String(005) | Sim | Código da transação padrão para NF cobrança fora do estado |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodEdc | String(003) | Sim | Espécie de documento para fins fiscais |
| CodMoe | String(003) | Sim | Código da moeda ou índice |
| DepNfv | String(010) | Sim | Código do depósito padrão para geração do cupom fiscal. |
| IndExc | String(001) | Sim | Indicativo se deve excluir os registros após a importação. |
| TipArm | Number(001,0) | Não | Tipo de Armazenagem |
| IndPro | String(001) | Não | Indicativo se o produto é importado com situação inativa |
| EpfWms | String(001) | Sim | Indicativo se deve exportar o documento ao sistema WMS no seu fechamento |
| TnsTit | String(005) | Sim | Código da transação padrão para movimento de título |
| IntRez | String(001) | Sim | Indicativo se integra redução Z |
| IndZer | String(001) | Sim | Indicativo se exporta produto com valor zero |
| NumMed | Number(001,0) | Sim | Unidade de Medida para exportação |
| RegAnt | Number(004,0) | Sim | Código da regra que deve ser executada antes de importar |
| RegDep | Number(004,0) | Sim | Código da regra que deve ser executada depois de importar |
| FilWms | Number(010,0) | Sim | Código do Estabelecimento |
| IndFaz | String(001) | Sim | Indicativo se a Filial é uma Fazenda |
| DirDav | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação referente ao DAV |
| IntSag | String(001) | Sim | Indicativo se a empresa/filial possui integração logística |
| SnfDev | String(003) | Sim | Código da série de notas fiscais de devolução |
| TnpDev | String(005) | Sim | Código da transação para devolução de mercadorias |
| TnsEem | String(005) | Sim | Código da transação para entrada manual de mercadorias do estoque |
| TnsEsm | String(005) | Sim | Código da transação para saída manual de mercadorias do estoque |
| TnsEeb | String(005) | Sim | Código da transação para entrada de bloqueio de mercadorias do estoque |
| TnsEsb | String(005) | Sim | Código da transação para saída de bloqueio de mercadorias do estoque |
| TnsEer | String(005) | Sim | Código da transação para entrada de reserva de mercadorias do estoque |
| TnsEsr | String(005) | Sim | Código da transação para saída de reserva de mercadorias do estoque |
| TnsStr | String(005) | Sim | Código da transação para saída por transferência de mercadorias entre depósitos |
| TnsEao | String(005) | Sim | Transação de estoque para estorno de produto acabado da OP |
| TnsQes | String(005) | Sim | Transação de estoque para saída do estorno de inspeção de qualidade |
| TnsQee | String(005) | Sim | Transação de estoque para entrada do estorno de inspeção de qualidade |
| ExpDls | String(001) | Sim | Obriga que o sistema WMS utilize os lotes/séries do ERP na expedição? |
| RecDls | String(001) | Sim | Obriga que o sistema WMS utilize os lotes/séries do ERP no recebimento? |
| MtvBlq | String(250) | Sim | Código do motivo de bloqueio no WMS para movimentos de bloqueio. |
| MtvRsv | String(250) | Sim | Código do motivo de bloqueio no WMS para movimentos de reserva. |
| BlqPed | String(001) | Sim | Indicativo se o sistema deve exigir estoque para enviar pedidos para separação |
| MotBlq | Number(006,0) | Sim | Código do motivo para bloqueio de pedido por falta de estoque |
| MotBfl | Number(006,0) | Sim | Código do motivo para bloqueio de pedido por falta de lote |
| SpfCpe | String(001) | Sim | Cancela o saldo do item de pedido na separação de pré-fatura do WMS a menos |
| SpfNsa | String(001) | Sim | Faturar pedidos e pré-faturas após retorno de separação do WMS |
| DocSep | Number(001,0) | Sim | Documento que será utilizado para gerar ordem de separação |
| NotApr | Number(001,0) | Sim | Número de nota a ser gravado no WMS para os apontamento de produção |
| EmiNfe | String(001) | Sim | Emite a NF-e gerada automaticamente após a separação do WMS |
| ExpGrd | String(001) | Sim | Indicativo se deve exportar os produtos em grade ao sistema WMS |
| TnsSiv | String(005) | Sim | Transação saída inicialização lote no inventário |
| TnsEiv | String(005) | Sim | Transação entrada inicialização lote no inventário |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
