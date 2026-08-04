# E046NEI

## Descrição

Notas Explicativas - Imagens

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| GruNex | String(030) | Não | Grupo de notas explicativas |
| CodImg | String(020) | Não | Código da imagem |
| DesImg | String(250) | Sim | Descrição da imagem |
| ImgFot | Image | Sim | Imagem a ser utilizada nas notas explicativas do grupo |
| EndImg | String(255) | Sim | Endereço da imagem utilizada no grupo, a qual não esta gravada no banco de dados |

---

## Chave Primária

- CodEmp
- GruNex
- CodImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E046NEI_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E046NEI_001

**Tabela:** E046GNE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| GruNex | GruNex |

