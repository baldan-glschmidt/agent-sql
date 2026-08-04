# E085CXC

## Descrição

Cadastros - Clientes - Ligação Cliente X Tipos de Contas

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodTcc | String(003) | Não | Código do tipo de conta |
| NumCco | String(014) | Não | Número da Conta Interna |
| DatCad | Date | Sim | Data do Cadastro |
| DatEnc | Date | Sim | Data do Encerramento |
| ObsCxc | String(250) | Sim | Observação da ligação |
| SitCxc | String(001) | Sim | Indicativo da situação |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| DatGer | Date | Sim | Data de geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodCli
- CodTcc
- NumCco

---

## Índices

### E085CXCIndice1

**Tipo:** Não unico

Campos:
- CodCli

### E085CXCIndice2

**Tipo:** Não unico

Campos:
- CodTcc

---

## Relacionamentos

### IR_E085CXC_001

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085CXC_002

**Tabela:** E034TCC

| Origem | Destino |
|--------|---------|
| CodTcc | CodTcc |

