# E075LPF

## Descrição

Cadastros - Produtos - Liga Fotos aos Produtos

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodPro | String(014) | Não | Código do Produto  associado a Foto |
| CodDer | String(007) | Não | Derivação do  Produto |
| SeqLpf | Number(004,0) | Não | Sequência de Fotos ligada ao Produto |
| FotPro | String(014) | Não | Código da Foto |
| FotDer | String(007) | Sim | Derivação da Foto |
| SeqFot | Number(004,0) | Não | Número de Sequência da Foto no Cadastro de Fotos |
| DatGer | Date | Sim | Data da Geração da ligação Produto X Foto |
| SeqCmd | Number(007,0) | Não | Sequência do componente na máscara de Derivação |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- SeqLpf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075LPF_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

