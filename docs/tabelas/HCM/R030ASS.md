# R030ASS

## Descrição

Empresa - Assinalamentos

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatAlt | Date | Não | Data da Alteração |
| OpcInt | Number(001,0) | Sim | Período Férias na Troca Categoria Intermitente |
| AfaSim | String(001) | Sim | Verificar Afastamentos Rescisão Simulada |
| PdfEco | Number(004,2) | Sim | % Provisão de desconto de férias do empregado - Crédito do Trabalhador |
| FcpFct | Number(001,0) | Sim | Provisão de férias - Crédito do Trabalhador |

---

## Chave Primária

- NumEmp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030ASS_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

