# E073VTR

## Descrição

Cadastros - Transportadoras - Histórico de Alteração Fiscal da Transportadora

---

## Resumo

- Campos: 28
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| DatAtu | Date | Não | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Não | Hora/minuto da última atualização do cadastro |
| SeqAtu | Number(003,0) | Não | Sequência da atualização |
| NomTra | String(100) | Não | Nome da transportadora |
| ApeTra | String(050) | Sim | Nome fantasia da transportadora - descontinuado |
| TipTra | String(001) | Não | Tipo de transportadora |
| InsEst | String(025) | Sim | Inscrição estadual da transportadora |
| InsMun | String(016) | Sim | Inscrição municipal da transportadora |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF da transportadora |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF da transportadora |
| EndTra | String(100) | Sim | Endereço da transportadora |
| CplEnd | String(200) | Sim | Complemento do endereço da transportadora (sala, andar, etc.) |
| CepTra | Number(008,0) | Sim | Cep da transportadora |
| BaiTra | String(075) | Sim | Bairro da transportadora |
| CidTra | String(060) | Sim | Cidade da transportadora |
| SigUfs | String(002) | Sim | Sigla do estado da transportadora |
| CodVia | String(003) | Não | Código da via de transporte da transportadora |
| TraCli | Number(009,0) | Sim | Código da transportadora como cliente |
| TraFor | Number(009,0) | Sim | Código da transportadora como fornecedor |
| SitTra | String(001) | Não | Situação da transportadora |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| DatFis | Date | Sim | Data da última atualização da data fiscal |
| DatFat | Date | Sim | Data da última alteração da data fiscal |
| UsuFat | Number(010,0) | Sim | Usuário da última alteração da data fiscal |
| HorFat | Number(005,0) | Sim | Hora da última alteração da data fiscal |
| CodPai | String(004) | Sim | Código do país da transportadora |

---

## Chave Primária

- CodTra
- DatAtu
- HorAtu
- SeqAtu

---

## Índices

### E073VTRIndice1

**Tipo:** Não unico

Campos:
- CgcCpf
- InsEst
- DatAtu
- HorAtu
- SeqAtu

### E073VTRIndice2

**Tipo:** Não unico

Campos:
- DocIde
- InsEst
- DatAtu
- HorAtu
- SeqAtu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
