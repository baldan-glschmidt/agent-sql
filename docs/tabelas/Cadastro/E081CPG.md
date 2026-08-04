# E081CPG

## Descrição

Tabelas - Atributos da Venda - Condições - Condições de pagamento

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdcCpg | Number(009,0) | Não | Índice da condição de pagamento na condição do atributo de venda |
| IdcIac | Number(009,0) | Não | Índice das condições do atributo de venda |
| CodCpg | String(006) | Sim | Código da condição de pagamento |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(009,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsCpg | String(099) | Sim | Observação da condição de pagamento |
| SitReg | String(001) | Não | Situação da condição de pagamento na condição do atributo de venda |

---

## Chave Primária

- IdcCpg

---

## Índices

### E081CPG_UNIQUE

**Tipo:** Unico

Campos:
- IdcIac
- CodCpg

---

## Relacionamentos

Nenhum relacionamento cadastrado.
