# E084CPJ

## Descrição

Cadastros - Máscara Projeto - Componentes

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMpj | String(008) | Não | Código da Máscara |
| CodCpj | String(020) | Não | Código do Componente da Máscara de Projeto |
| SeqCpj | Number(004,0) | Não | Número Sequencial dos componentes da máscara |
| DesCpj | String(020) | Não | Descrição do Componente da Máscara |
| AbrCpj | String(010) | Não | Abreviatura do Componente da Máscara |
| SitCpj | String(001) | Não | Situação do componente da máscara de projeto |

---

## Chave Primária

- CodEmp
- CodMpj
- CodCpj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084CPJ_001

**Tabela:** E084MPJ

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpj | CodMpj |

