# E055CTB

## Descrição

Tabelas - Impostos - Parâmetro Contábil Formação Base Impostos

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| CtaRed | Number(007,0) | Não | Conta contábil reduzida |
| VlrDeb | String(001) | Não | Opção do cálculo a ser efetuado com o valor dos lançamentos devedores |
| VlrCre | String(001) | Não | Opção do cálculo a ser efetuado com o valor dos lançamentos credores |
| VlrSal | String(001) | Não | Opção do cálculo a ser efetuado com o valor do saldo contábil da conta |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- CtaRed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055CTB_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

