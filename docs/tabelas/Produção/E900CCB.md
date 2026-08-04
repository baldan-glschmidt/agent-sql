# E900CCB

## Descrição

O.P./O.S. - Contagem das quantidades da O.P./O.S. via código de barras

---

## Resumo

- Campos: 20
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do produto/serviço fabricado na O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqRot | Number(004,0) | Não | Sequência lógica da Operação no Roteiro de Produção |
| SeqEoq | Number(005,0) | Não | Sequência da movimentação da produção |
| NumGop | Number(004,0) | Sim | Número da guia associada a quantidade informada |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Derivação do Produto |
| QtdRe1 | Number(014,5) | Sim | Quantidade real de 1ª qualidade no Estágio |
| QtdRe2 | Number(014,5) | Sim | Quantidade real de 2ª qualidade no Estágio |
| QtdRe3 | Number(014,5) | Sim | Quantidade real de 3ª qualidade no Estágio |
| QtdRfg | Number(014,5) | Sim | Quantidade de Refugo |
| QtdIql | Number(014,5) | Sim | Quantidade Retirada p/ Inspeção de Qualidade |
| DatRea | Date | Não | Data da efetivação (data fim do processo de fabricação) |
| HorRea | Number(005,0) | Sim | Hora da efetivação (hora fim do processo de fabricação) |
| NumCad | Number(009,0) | Sim | Número do Cadastro do Operador |
| CodUsu | Number(010,0) | Sim | Código do Usuário  que deu a entrada no Estoque (Último Estágio) |
| CodRef | String(050) | Sim | Código da Referência para Controles Diversos |
| IndMov | String(001) | Sim | Indica se esta quantidade já foi movimentada na Produção |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqRot
- SeqEoq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900CCB_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900CCB_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E900CCB_008

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

