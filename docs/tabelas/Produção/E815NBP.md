# E815NBP

## Descrição

PCP - Necessidades Produtos

---

## Resumo

- Campos: 52
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da Filial do Pedido |
| NumPed | Number(008,0) | Não | Número do Pedido (Quando Pedido = 0, é Necessidade agrupada) |
| SeqIpd | Number(004,0) | Não | Item do Pedido (Quando p/ Pedido específico) |
| CodPvp | String(008) | Não | Código do Período |
| CodPro | String(014) | Não | Código do Produto |
| CodDer | String(007) | Não | Código de Derivação do Produto |
| PvpPai | String(008) | Não | Código do Período gerador (Procedente) quando é necessário produtos intermediários |
| AgrNec | String(025) | Não | Agrupamento de necessidades |
| AgrPai | String(025) | Não | Agrupamento de necessidades pai |
| CodOri | String(003) | Não | Código de Origem do Produto |
| CodFam | String(006) | Não | Código da Família do Produto |
| UniMed | String(003) | Não | Unidade de Medida do produto |
| QtdNec | Number(014,5) | Não | Quantidade Necessária Efetiva |
| QtdXpl | Number(014,5) | Sim | Quantidade Explodida no Cálculo de Necessidades (Já feito a Explosão de Nec.) |
| QtdOrp | Number(014,5) | Sim | Quantidade total de OPs geradas, para suprir a necessidade |
| SldOrp | Number(014,5) | Sim | Saldo de OPs em aberto na Produção (em processo) |
| SbrOrp | Number(014,5) | Sim | Quantidade de OPs sobressalentes geradas sem Cálculo de Explosão |
| QtdCan | Number(014,5) | Sim | Quantidade Cancelada da Necessidade Calculada |
| CanXpl | Number(014,5) | Sim | Quantidade  Necessária Explodida que foi Cancelada |
| CanOrp | Number(014,5) | Sim | Quantidade Cancelada de OPs já geradas |
| QtdRes | Number(014,5) | Sim | Quantidade Reservada no Estoque (Quando abate estoque disponível) |
| QtdRca | Number(014,5) | Não | Quantidade original no Cálculo de Reservas no estoque |
| QtdOri | Number(014,5) | Sim | Quantidade original necessária sem abatimento estoque disponível |
| DisUti | Number(014,5) | Sim | Quantidade original necessária sem abatimento estoque disponível |
| QtdCal | Number(014,5) | Não | Quantidade original do Cálculo de Necessidades |
| QtdAnt | Number(014,5) | Sim | Quantidade Necessária Anterior (Última alteração manual) |
| GerOrp | String(001) | Não | Gera Ordem de Produção (S=Sim, N=Não) |
| GerNec | Number(001,0) | Não | Gerou Necessidade compra e produto intermediário (semi-acabado) |
| QtdDia | Number(006,2) | Não | Quantidade dias de produção p/ produto pai desta necessidade calculada |
| TipNec | String(001) | Não | Tipo de Necessidade de Produto (Fabricado) |
| CodDep | String(010) | Sim | Código do Depósito que foi efetuado a reserva de estoque |
| SeqCmd | Number(007,0) | Sim | Sequência da Derivação na Máscara do Produto |
| CodUsu | Number(010,0) | Não | Código do Usuário que  Atualizou o Registro |
| DatAtu | Date | Não | Data da Atualização do Registro |
| HorAtu | Number(005,0) | Sim | Hora da Atualização do Registro |
| SitNbp | String(001) | Sim | Indicativo se a Necessidade Produto poderá ser Gerada Explosão de Necessidades/OPs |
| QtdRe2 | Number(014,5) | Sim | Quantidade Realizada de 2ª Qualidade |
| QtdRe3 | Number(014,5) | Sim | Quantidade Realizada de 3ª Qualidade |
| QtdRfg | Number(014,5) | Sim | Quantidade Realizada de Refugos |
| QtdIql | Number(014,5) | Sim | Quantidade Inspecionada (Não disponível em Estoque) |
| GerCga | String(001) | Não | Indicativo se Necessidade foi considerada na Carga de Recursos |
| IndAlt | String(001) | Não | Indicativo se Necessidade foi alterada |
| ProEqi | String(014) | Sim | Produto Equivalente vinculado a este Titular |
| DerEqi | String(007) | Sim | Derivação do Produto equivalente |
| SldNec | Number(014,5) | Sim | Saldo de Necessidades gerado a mais pelo calculo proveniente da quantidade mínima |
| AgrExp | String(020) | Sim | Agrupamento do cálc. de necessidades para identificação multinível de um lote explosão |
| QtdSol | Number(014,5) | Sim | Quantidade de Solicitações geradas p/ suprir esta Necessidade (Quando produto é misto e não gera OP) |
| NumPri | Number(004,0) | Sim | Número da Prioridade da Necessidade para Geração da O.P. |
| USU_DatAtu | Date | Sim | Data da Atualização do Registro - Baldan |
| USU_HorAtu | Number(005,0) | Sim | Hora da Atualização do Registro - Baldan |
| USU_NumSea | Number(009,0) | Sim | SEA gerada para atender necessidade |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd
- CodPvp
- CodPro
- CodDer
- PvpPai
- AgrNec
- AgrPai

---

## Índices

### E815NBPindice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumPed
- SeqIpd
- CodPvp
- ProEqi
- DerEqi
- CodPro
- CodDer
- PvpPai
- AgrNec
- AgrPai

---

## Relacionamentos

### IR_E815NBP_004

**Tabela:** E016PVP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPvp | CodPvp |

### IR_E815NBP_006

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E815NBP_010

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

### IR_E815NBP_011

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E815NBP_012

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

