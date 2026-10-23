# R084ANE

## Descrição

Plano de Ação - Anexos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |
| SeqArq | Number(003,0) | Não | Sequência do arquivo |
| NomArq | String(250) | Sim | Nome do arquivo de anexo |
| DesArq | String(060) | Sim | Descrição do anexo |
| ArqAne | Image | Sim | Anexo |

---

## Chave Primária

- NumEmp
- CodPln
- SeqArq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R084ANE_001

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

