# E090RCP

## Descrição

Cadastros - Representantes - Ligação Representante X Condição Pagamento

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
| EmpCpg | Number(004,0) | Não | Código da empresa da Condição de Pagamento |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| SitLrc | String(001) | Sim | Situação da ligação |
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
- EmpCpg
- CodCpg

---

## Índices

### E090RCPIndice1

**Tipo:** Não unico

Campos:
- EmpCpg
- CodCpg

---

## Relacionamentos

### IR_E090RCP_003

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| EmpCpg | CodEmp |
| CodCpg | CodCpg |

