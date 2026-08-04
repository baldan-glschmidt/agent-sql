# E031VMM

## Descrição

Tabelas - Moedas - Valorização Multimoeda

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMoe | String(003) | Não | Código da moeda ou índice |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| DatIni | Date | Não | Data início da valorização multimoeda |
| DatFim | Date | Não | Data final da valorização multimoeda |
| SeqVmm | Number(003,0) | Não | Sequência da valorização da multimoeda |
| CotIni | Number(017,8) | Sim | Valor da cotação do período inicial da valorização |
| CotFim | Number(017,8) | Sim | Valor da cotação do período final da valorização |

---

## Chave Primária

- CodMoe
- CodEmp
- CodFil
- DatIni
- DatFim
- SeqVmm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E031VMM_000

**Tabela:** E031MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

