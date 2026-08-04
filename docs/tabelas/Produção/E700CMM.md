# E700CMM

## Descrição

Ficha - Modelo - Componentes

---

## Resumo

- Campos: 47
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde  o componente é agregado ao Produto composto |
| SeqMod | Number(004,0) | Não | Sequência lógica que o componente é utilizado na fabricação do Produto composto |
| CodCmp | String(014) | Não | Código do Componente(Produto) agregado |
| DesCmp | String(100) | Sim | Descrição complementar sobre a utilização do componente |
| VarDer | String(001) | Não | Derivação é Variável de um Produto p/ outro (deve ser ligado Produto X Modelo) |
| NecLig | String(001) | Não | Componente Necessita ser ligado ao Produto específico que o utiliza |
| TipQtd | String(001) | Não | Tipo de Quantidade Utilizada (P=Proporcional - À Quantidade Base, F=Fixa - Ao Lote Técnico do Roteiro, R=Frequencial - À Quantidade Frequencial do Produto) |
| TipRdm | String(001) | Sim | Tipo de rendimento para o calculo da variação do consumo |
| VlrRdm | Number(014,5) | Sim | Valor do rendimento para ser aplicado a variação do consumo |
| DtiVal | Date | Sim | Data de Validade inicial p/ utilização deste componente (Opcional) |
| DtfVal | Date | Sim | Data de Validade final p/ utilização deste componente (Opcional) |
| SeqSbs | Number(004,0) | Sim | Sequência para ser Substituída, conforme data de validade |
| SbsPro | String(014) | Sim | Utiliza este componente somente p/ o Produto Composto especificado |
| SbsCli | Number(009,0) | Sim | Usa este componente somente p/ o Cliente especificado (quando Pedido não for agrupado no Cálculo Necessidades) |
| CodGre | Number(009,0) | Sim | Usa este componente somente para o grupo de cliente especificado (quando pedido não for agrupado no cálculo necessidades) |
| DatAlt | Date | Não | Data Geração ou Alteração da sequência |
| IndPep | String(001) | Não | Qual a forma que a explosão de necessidades considera a Quantidade/Perda informada no componente |
| IndEqi | String(001) | Não | Indicativo se o componente é equivalente ao relacionado ao campo "Substitui a Sequência" |
| CodCcu | String(009) | Sim | Código do Centro de Custos |
| CodUsu | Number(010,0) | Sim | Código do Usuário que alterou |
| ObsCmm | String(240) | Sim | Observações |
| SelPro | String(001) | Não | Indica se o item será considerado para a área de manufatura (Nec. e Geração de OPs). |
| SelCus | String(001) | Não | Indica se o item será considerado para a área de custos (importação da ficha técnica). |
| EnvCli | String(001) | Sim | Define se o componente foi ou não enviado pelo Cliente |
| IndEos | String(001) | Sim | Componente é do tipo saída (consumo) ou entrada (originado de algum produto ou componente) |
| CmpPen | String(001) | Sim | Parâmetro genérico para indicar se o componente é pendente ou não. |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| IndCob | String(001) | Sim | Indicativo se componente é cobrado |
| TolPes | Number(005,3) | Sim | % tolerância do peso líquido do produto ou do lote |
| FrmBxa | String(001) | Sim | Indica se a forma da baixa de componente será automática ou manual |
| CodClc | String(010) | Sim | Código da coleção |
| SeqVlc | Number(004,0) | Sim | Sequência da Validade da Coleção |
| USU_TipMer | String(001) | Sim | Tipo Mercado |
| USU_ordem | Number(003,0) | Sim | Ordem de carga |
| USU_KitSeq | Number(004,0) | Sim | Sequencia Montagem Kit |
| USU_KidCod | String(020) | Sim | Código Kit |
| USU_CodCxa | Number(005,0) | Sim | Codigo da Caixa de Transporte do Corrinho |
| USU_nrocxa | Number(005,0) | Sim | Número da Caixa |
| USU_CodCre | String(008) | Sim | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| USU_IndRel | String(001) | Sim | Indicativo Relacionamento |
| USU_CodCar1 | Number(005,0) | Sim | USU_CodCar1 |
| USU_SeqCar | Number(004,0) | Sim | Sequencia do Carrinho |
| USU_SeqRot | Number(004,0) | Sim | Seqüência lógica da operação no roteiro de produção |
| USU_IMOBI | String(001) | Sim | Imobilizado |

---

## Chave Primária

- CodEmp
- CodMod
- CodEtg
- SeqMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700CMM_001

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

### IR_E700CMM_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E700CMM_004

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCmp | CodPro |

