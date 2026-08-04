# E000ATN

## Descrição

Tabelas - Integrações - Registro de alterações de títulos do autenticador externo

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitExp | String(001) | Sim | Situação do processamento da pendência de integração |
| DatExp | Date | Sim | Data da exportação |
| HorExp | Number(005,0) | Sim | Hora da exportacao do registro |
| VctOan | Date | Não | Data do vencimento original anterior à alteracao |
| VctPan | Date | Não | Data do vencimento prorrogado anterior à alteração |
| VctOdp | Date | Não | Data do vencimento original posterior à alteração |
| VctPdp | Date | Não | Data do vencimento prorrogado posterior à alteração |

---

## Chave Primária

- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
