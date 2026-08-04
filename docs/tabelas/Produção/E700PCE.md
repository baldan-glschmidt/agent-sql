# E700PCE

## Descrição

Ficha - Modelo - Componentes Exclusivos para Fabricar Pedido/Item

---

## Resumo

- Campos: 32
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial do Pedido p/ uso exclusivo desse componente |
| NumPed | Number(008,0) | Não | Uso Exclusivo p/ fabricação do pedido (componentes) |
| SeqIpd | Number(004,0) | Não | Componente p/ uso Exclusivo p/ fabricação da Sequência de item do pedido |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde o componente é agregado ao Produto do Pedido |
| SeqMod | Number(004,0) | Não | Sequência do Modelo usada p/ o Pedido/Item |
| SeqPce | Number(004,0) | Não | Sequência lógica que o componente é utilizado na fabricação do Produto do Pedido |
| CodMod | String(014) | Sim | Código do Modelo associado ao Produto |
| CodCmp | String(014) | Não | Código do Componente (Produto) agregado |
| DerCmp | String(007) | Sim | Derivação do Componente FIXA (p/ todos os Produtos compostos que estão associado) |
| QtdUti | Number(014,5) | Não | Quantidade utilizada do componente (Proporcional/Fixa) |
| QtdFrq | Number(014,5) | Sim | Quantidade Frequencial (Produto produzido) que o componente é consumido (apropriado) |
| PerPrd | Number(006,3) | Sim | % Perda do componente no processo de fabricação |
| PrdQtd | Number(014,5) | Não | Quantidade de perda do componente no processo de fabricação |
| UniMe2 | String(003) | Não | Unidade de medida  do componente na Produção |
| TipQtd | String(001) | Não | Tipo de Quantidade Utilizada (P=Proporcional - À Quantidade Base, F=Fixa - Ao Lote Técnico do Roteiro, R=Frequencial - À Quantidade Frequencial do Produto) |
| DesCmp | String(100) | Sim | Descrição complementar sobre a utilização do componente no item do pedido |
| IndPep | String(001) | Não | Qual a forma que a explosão de necessidades considera a Quantidade/Perda informada no componente |
| IndIae | String(001) | Não | Indicativo se o Registro Altera/Inclui/Exclui o componente da Estrutura do produto |
| DatAlt | Date | Não | Data Geração ou Alteração da sequência |
| CodCcu | String(009) | Sim | Código do Centro de Custos |
| CodUsu | Number(010,0) | Sim | Código do Usuário que alterou |
| ObsPec | String(240) | Sim | Observações |
| BxaOrp | String(001) | Sim | Se for componente de alguma OP, indica se o mesmo é baixado |
| CmpPen | String(001) | Sim | Parâmetro genérico para indicar se o componente é pendente ou não. |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| SbsPro | String(014) | Sim | Utiliza este componente somente p/ o Produto Composto especificado |
| CodDep | String(010) | Sim | Depósito em que foi efetuado a reserva de estoque |
| CodLot | String(050) | Sim | Lote de fabricação do componente (Produto Intermediário/Comprado) |
| SelPro | String(001) | Não | Indica se o item será considerado para a área de manufatura (Nec. e Geração de OPs). |
| SelCus | String(001) | Não | Indica se o item será considerado para a área de custos (importação da ficha técnica). |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd
- CodEtg
- SeqMod
- SeqPce

---

## Índices

### E700PCEIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodMod
- CodEtg
- SeqMod
- CodCmp
- DerCmp

---

## Relacionamentos

### IR_E700PCE_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

### IR_E700PCE_003

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

### IR_E700PCE_004

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E700PCE_008

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCmp | CodPro |

### IR_E700PCE_014

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMe2 | UniMed |

