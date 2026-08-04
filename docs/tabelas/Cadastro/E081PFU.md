# E081PFU

## Descrição

Tabelas - Atributos da Venda - Condições - Perfis de Usuário

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdcIac | Number(009,0) | Não | Índice das condições do atributo de venda |
| CodPer | Number(009,0) | Não | Código do Perfil |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| SitReg | String(001) | Não | Situação do perfil de usuário na condição do atributo de venda |

---

## Chave Primária

- IdeUni

---

## Índices

### E081PFUIndice1

**Tipo:** Unico

Campos:
- IdcIac
- CodPer

### E081PFUIndice2

**Tipo:** Não unico

Campos:
- CodPer

---

## Relacionamentos

### IR_E081PFU_001

**Tabela:** E081IAC

| Origem | Destino |
|--------|---------|
| IdcIac | IdcIac |

### IR_E081PFU_002

**Tabela:** E000PFU

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

