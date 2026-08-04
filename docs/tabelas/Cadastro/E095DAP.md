# E095DAP

## Descrição

Cadastros - Fornecedores - DAP - Declaração de Aptidão ao Pronaf

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDap | String(025) | Não | Código da DAP - Declaração de Aptidão ao Pronaf |
| EnqDap | String(010) | Não | Código de enquadramento da DAP |
| DatVal | Date | Não | Data de validade da DAP |
| DatEmi | Date | Não | Data de emissão da DAP |
| VerDap | String(010) | Não | Versão da DAP |
| CpfTi1 | Number(012,0) | Não | Número do CPF do 1º titular da DAP |
| CpfTi2 | Number(012,0) | Sim | Número do CPF do 2º titular da DAP |
| CndPut | String(250) | Não | Condições de posse e uso da terra |
| CgcEmi | Number(014,0) | Não | Número do CNPJ do emissor da DAP |
| DocIdeEmi | String(014) | Sim | Número do CNPJ do emissor da DAP |
| CidDap | String(060) | Não | Cidade da DAP |
| UfsDap | String(002) | Não | Sigla do Estado da DAP |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodDap

---

## Índices

### E095DAPIndice2

**Tipo:** Não unico

Campos:
- CpfTi1

### E095DAPIndice3

**Tipo:** Não unico

Campos:
- CpfTi2

### E095DAPIndice4

**Tipo:** Não unico

Campos:
- UfsDap

---

## Relacionamentos

### IR_E095DAP_011

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| UfsDap | SigUfs |

