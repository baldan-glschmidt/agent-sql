# E002PVM

## Descrição

Cadastros - Finanças - Parâmetros Ajuste a Valor de Mercado

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador dos parâmetros do ajuste |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SitReg | String(001) | Não | Situação do registro |
| AplPar | String(001) | Sim | Indica o módulo de destino dos parâmetros |
| VlrMin | Number(015,2) | Sim | Valor mínimo do título para o cálculo do ajuste a valor de mercado |
| QtdTpc | Number(009,0) | Não | Quantidade de títulos por pacote de processamento do cálculo |
| TipCal | String(001) | Não | Tipo de cálculo do ajuste a valor de mercado |
| TnsPos | String(005) | Não | Transação padrão para ajuste a valor de mercado positivo |
| TnsNeg | String(005) | Não | Transação padrão para ajuste a valor de mercado negativo |
| TnsEps | String(005) | Não | Transação padrão para estorno de ajuste a valor de mercado positivo |
| TnsEng | String(005) | Não | Transação padrão para estorno de ajuste a valor de mercado negativo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E002PVMIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- AplPar

---

## Relacionamentos

Nenhum relacionamento cadastrado.
