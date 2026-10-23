# R030HOM

## Descrição

Filiais da Empresa - Configurações do HomologNet

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| SinPat | Number(001,0) | Sim | Sindicato Patronal |
| CodSin | Number(004,0) | Sim | Código do Sindicato |
| NumCgc | Number(015,0) | Sim | Número do CNPJ Sindicato |
| CfjCgc | String(014) | Sim | Número do CNPJ Sindicato |
| CodEnt | Number(012,0) | Sim | Código da Entidade Sindical |
| UsaHom | String(001) | Sim | Utiliza HomologNet |
| EntAlf | String(020) | Sim | Código da Entidade Sindical Alfanumérico |

---

## Chave Primária

- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030HOM_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

