# E076LML

## Descrição

Cadastros - Marcas - Ligação Marca X Lista de Preço

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMar | String(010) | Não | Código da Marca/Etiqueta |
| EmpLip | Number(004,0) | Não | Código da empresa da Lista de Preço |
| CodLip | String(005) | Não | Código da lista de preço utilizada na venda |
| VenDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de venda |
| SitLml | String(001) | Não | Situação da ligação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da útima altualização do cadastro |

---

## Chave Primária

- CodMar
- EmpLip
- CodLip

---

## Índices

### E076LMLIndice1

**Tipo:** Não unico

Campos:
- EmpLip
- CodLip

---

## Relacionamentos

### IR_E076LML_000

**Tabela:** E076MAR

| Origem | Destino |
|--------|---------|
| CodMar | CodMar |

### IR_E076LML_002

**Tabela:** E028LIP

| Origem | Destino |
|--------|---------|
| EmpLip | CodEmp |
| CodLip | CodLip |

