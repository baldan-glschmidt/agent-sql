# E090RLI

## Descrição

Cadastros - Representantes - Ligação Representante X Lista de Preços

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| CodMar | String(010) | Não | Código da Marca/Etiqueta vinculada a um produto ou a um pedido |
| EmpLip | Number(004,0) | Não | Código da empresa da lista de preço |
| CodLip | String(005) | Não | Código da lista de preço utilizada na venda |
| SitLrt | String(001) | Sim | Situação da ligação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodRep
- CodMar
- EmpLip
- CodLip

---

## Índices

### E090RLIIndice1

**Tipo:** Não unico

Campos:
- EmpLip
- CodLip

---

## Relacionamentos

### IR_E090RLI_003

**Tabela:** E028LIP

| Origem | Destino |
|--------|---------|
| EmpLip | CodEmp |
| CodLip | CodLip |

