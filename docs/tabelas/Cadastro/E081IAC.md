# E081IAC

## Descrição

Tabelas - Atributos da Venda - Condições

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdcIac | Number(009,0) | Não | Índice das condições do atributo de venda |
| IdcAtv | Number(009,0) | Não | Índice do atributo da venda |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(009,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsIac | String(099) | Sim | Observação da condição |
| SitReg | String(001) | Não | Situação da condição do atributo de venda |
| DesIac | String(010) | Não | Descrição da condição |
| IndAcu | String(001) | Sim | Indicativo se a condição é acumulativa com ela mesma |
| IndAoc | String(001) | Sim | Indica se a condição é acumulativa com outras condições e outras promoções |

---

## Chave Primária

- IdcIac

---

## Índices

### E081IAC_UNIQUE

**Tipo:** Unico

Campos:
- IdcAtv
- IdcIac

---

## Relacionamentos

Nenhum relacionamento cadastrado.
