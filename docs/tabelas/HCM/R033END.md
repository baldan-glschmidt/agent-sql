# R033END

## Descrição

Pessoas - Endereços

---

## Resumo

- Campos: 17
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| TipEnd | Number(001,0) | Não | Tipo de endereço |
| DatAlt | Date | Não | Data de Alteração |
| TipLgr | String(005) | Sim | Tipo do Logradouro |
| EndRua | String(100) | Sim | Endereço Residencial |
| EndNum | String(006) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento Endereço |
| CodCid | Number(007,0) | Sim | Cidade |
| CodBai | Number(004,0) | Sim | Bairro |
| EndCep | Number(008,0) | Sim | CEP |
| EmpAux | Number(004,0) | Sim | USO EXCLUSIVO SENIOR |
| TipAux | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CadAux | Number(009,0) | Sim | USO EXCLUSIVO SENIOR |
| DepAux | Number(002,0) | Sim | USO EXCLUSIVO SENIOR |
| ColAti | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CanAux | Number(007,0) | Sim | USO EXCLUSIVO SENIOR |
| DatAux | Date | Sim | USO EXCLUSIVO SENIOR |

---

## Chave Primária

- CodPes
- TipEnd
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033END_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

