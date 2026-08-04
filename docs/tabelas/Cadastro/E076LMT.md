# E076LMT

## Descrição

Cadastros - Marcas - Ligação Marca X Tabela de Preço

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMar | String(010) | Não | Código da Marca/Etiqueta |
| EmpTpr | Number(004,0) | Não | Código da empresa da Tabela de Preço |
| CodTpr | String(004) | Não | Código da tabela de preço |
| SitLmt | String(001) | Não | Situação da ligação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da útima altualização do cadastro |

---

## Chave Primária

- CodMar
- EmpTpr
- CodTpr

---

## Índices

### E076LMTIndice1

**Tipo:** Não unico

Campos:
- EmpTpr
- CodTpr

---

## Relacionamentos

### IR_E076LMT_000

**Tabela:** E076MAR

| Origem | Destino |
|--------|---------|
| CodMar | CodMar |

### IR_E076LMT_002

**Tabela:** E081TAB

| Origem | Destino |
|--------|---------|
| EmpTpr | CodEmp |
| CodTpr | CodTpr |

